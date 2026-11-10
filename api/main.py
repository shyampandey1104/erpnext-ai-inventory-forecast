"""FastAPI application for AI Inventory Forecasting."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from forecast_engine.model import DemandForecastEngine

app = FastAPI(
    title="ERPNext AI Inventory Forecast Engine",
    description="Machine Learning demand forecasting & smart reorder point calculation for ERPNext items.",
    version="1.0.0",
)

engine = DemandForecastEngine()


class ForecastRequest(BaseModel):
    item_code: str
    historical_monthly_sales: List[float]
    lead_time_days: int = 15
    current_stock: float = 50.0
    horizon_months: int = 3


@app.post("/api/v1/forecast/predict")
async def predict_demand(req: ForecastRequest):
    """Generate multi-month demand forecast and reorder recommendations."""
    if len(req.historical_monthly_sales) < 3:
        raise HTTPException(status_code=400, detail="Minimum 3 months of historical sales required for forecast.")

    forecast = engine.exponential_smoothing_forecast(
        req.historical_monthly_sales, horizon_months=req.horizon_months
    )
    reorder_params = engine.calculate_reorder_parameters(
        req.historical_monthly_sales,
        lead_time_days=req.lead_time_days,
        current_stock=req.current_stock,
    )

    return {
        "item_code": req.item_code,
        "historical_sales": req.historical_monthly_sales,
        "projected_sales_next_months": forecast,
        "inventory_intelligence": reorder_params,
    }


@app.get("/")
async def root():
    return {
        "service": "ERPNext AI Inventory Forecasting Agent",
        "status": "online",
        "docs": "/docs",
    }
