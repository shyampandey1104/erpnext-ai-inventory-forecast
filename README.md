# 📈 ERPNext AI Inventory & Demand Forecast Engine

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com)
[![ERPNext](https://img.shields.io/badge/ERPNext-v14%20%7C%20v15-blue.svg)](https://erpnext.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An AI-driven **Demand Forecasting & Smart Reorder Point (ROP) Engine** for **ERPNext**. Ingests historical item sales, applies time-series exponential smoothing to model seasonality and trend, computes dynamic safety stocks using statistical Z-scores (95% service level), and auto-generates ERPNext **Material Request** records before inventory runs out.

---

## ⚡ Highlights

- 📊 **Time-Series Demand Prediction**: Multi-month future demand projections based on historical Sales Invoice data.
- 🛡️ **Dynamic Safety Stock & ROP**: Calculates exact Reorder Point considering lead time uncertainty:
  $$\text{ROP} = (\text{Lead Time} \times \text{Daily Demand}) + (Z \times \sqrt{\text{Lead Time}} \times \sigma_{\text{demand}})$$
- 🔄 **ERPNext Material Request Auto-Creation**: Creates draft purchase requisitions in ERPNext when stock falls below calculated ROP.
- 🌐 **Interactive REST API**: Ready-to-integrate FastAPI endpoints with Swagger docs.

---

## 🚀 Quickstart

```bash
git clone https://github.com/shyampandey1104/erpnext-ai-inventory-forecast.git
cd erpnext-ai-inventory-forecast
pip install -r requirements.txt
uvicorn api.main:app --reload --port 8000
```
Visit `http://localhost:8000/docs` to test forecasting interactively.

---

## 🧪 Running Tests

```bash
pytest tests/ -v
```

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

Author: **Shyamkumar Bhupendra Pandey** ([@shyampandey1104](https://github.com/shyampandey1104))
