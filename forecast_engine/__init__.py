"""ERPNext AI Inventory Demand Forecast Engine."""

from forecast_engine.model import DemandForecastEngine
from forecast_engine.erpnext_sync import ERPNextForecastSync

__version__ = "1.0.0"
__all__ = ["DemandForecastEngine", "ERPNextForecastSync"]
