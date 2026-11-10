"""ERPNext sync service for auto-creating Material Requests."""

import httpx
from typing import Dict, Any, Optional


class ERPNextForecastSync:
    def __init__(self, base_url: str, api_key: str, api_secret: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"token {api_key}:{api_secret}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    async def create_material_request(self, item_code: str, quantity: float, warehouse: str = "Stores - TC") -> Optional[str]:
        """Auto-generate Material Request DocType in ERPNext when stock breaches ROP."""
        payload = {
            "doctype": "Material Request",
            "material_request_type": "Purchase",
            "schedule_date": "2026-11-25",
            "items": [
                {
                    "item_code": item_code,
                    "qty": quantity,
                    "warehouse": warehouse,
                    "schedule_date": "2026-11-25",
                }
            ],
        }
        async with httpx.AsyncClient(timeout=10.0) as client:
            try:
                res = await client.post(
                    f"{self.base_url}/api/resource/Material Request",
                    headers=self.headers,
                    json=payload,
                )
                if res.status_code in (200, 201):
                    return res.json().get("data", {}).get("name")
            except Exception:
                pass
        return None
