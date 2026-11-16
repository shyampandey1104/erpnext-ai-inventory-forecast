# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "forecast_engine"
app_title = "Erpnext Ai Inventory Forecast"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Ai Inventory Forecast for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/forecast_engine/css/forecast_engine.bundle.css"
app_include_js = "/assets/forecast_engine/js/forecast_engine.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "forecast_engine.engine.on_document_submit",
        "on_cancel": "forecast_engine.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "forecast_engine.engine.daily_scheduled_sync"
    ]
}
