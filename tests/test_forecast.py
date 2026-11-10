"""Unit tests for DemandForecastEngine."""

from forecast_engine.model import DemandForecastEngine


def test_forecast_calculation():
    engine = DemandForecastEngine()
    history = [120.0, 135.0, 150.0, 140.0, 160.0, 175.0]
    forecast = engine.exponential_smoothing_forecast(history, horizon_months=3)

    assert len(forecast) == 3
    for f in forecast:
        assert f > 100.0


def test_reorder_point_trigger():
    engine = DemandForecastEngine()
    history = [200.0, 220.0, 210.0, 230.0]
    # Current stock is very low (10 units) -> Should trigger needs_reorder
    params = engine.calculate_reorder_parameters(history, lead_time_days=15, current_stock=10.0)

    assert params["needs_reorder"] is True
    assert params["reorder_point"] > 10.0
    assert params["recommended_order_qty"] > 0
