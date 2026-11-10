"""Time-series demand forecasting and Reorder Point (ROP) calculation engine."""

import math
from typing import List, Dict, Any, Tuple
import numpy as np


class DemandForecastEngine:
    """Calculates projected sales demand, safety stock, and Reorder Point (ROP)."""

    def __init__(self, service_level_z: float = 1.65):
        # 1.65 Z-score corresponds to ~95% service level / stockout protection
        self.z = service_level_z

    def exponential_smoothing_forecast(self, historical_sales: List[float], horizon_months: int = 3, alpha: float = 0.3) -> List[float]:
        """Simple exponential smoothing with trend dampening."""
        if not historical_sales:
            return [0.0] * horizon_months

        smoothed = [historical_sales[0]]
        for val in historical_sales[1:]:
            smoothed.append(alpha * val + (1 - alpha) * smoothed[-1])

        last_level = smoothed[-1]
        # Calculate recent average trend
        recent_trend = (historical_sales[-1] - historical_sales[0]) / max(len(historical_sales) - 1, 1) * 0.5

        forecasts: List[float] = []
        for i in range(1, horizon_months + 1):
            proj = max(0.0, last_level + (recent_trend * i))
            forecasts.append(round(proj, 1))

        return forecasts

    def calculate_reorder_parameters(
        self,
        historical_sales: List[float],
        lead_time_days: int = 15,
        current_stock: float = 100.0,
    ) -> Dict[str, Any]:
        """Compute Daily Demand, Demand Variance, Safety Stock, and Reorder Point (ROP)."""
        if not historical_sales:
            return {"safety_stock": 0.0, "reorder_point": 0.0, "recommended_order_qty": 0.0, "needs_reorder": False}

        # Assume monthly sales data -> convert to daily demand
        monthly_avg = float(np.mean(historical_sales))
        daily_demand = monthly_avg / 30.0

        monthly_std = float(np.std(historical_sales))
        daily_std = monthly_std / math.sqrt(30.0)

        # Safety Stock formula: Z * (sigma_L) = Z * sqrt(Lead_Time) * sigma_D
        safety_stock = self.z * math.sqrt(lead_time_days) * daily_std

        # Reorder Point (ROP) = (Lead Time * Daily Demand) + Safety Stock
        rop = (lead_time_days * daily_demand) + safety_stock

        needs_reorder = current_stock <= rop
        # Order quantity to cover 30 days demand + buffer
        recommended_order_qty = max(0.0, (monthly_avg * 1.5) - current_stock) if needs_reorder else 0.0

        return {
            "avg_monthly_demand": round(monthly_avg, 1),
            "avg_daily_demand": round(daily_demand, 2),
            "safety_stock": round(safety_stock, 1),
            "reorder_point": round(rop, 1),
            "current_stock": current_stock,
            "needs_reorder": needs_reorder,
            "recommended_order_qty": round(recommended_order_qty, 0),
        }
