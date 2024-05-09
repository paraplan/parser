from datetime import date
from typing import Any

from aiohttp import ClientSession
from aiohttp.connector import TCPConnector

from src.env import API_KEY, API_URL


async def _make_request(url: str, params: dict[str, Any]) -> bytes:
    async with ClientSession(connector=TCPConnector(verify_ssl=False)) as session:
        async with session.get(url, params=params) as resp:
            return await resp.read()


async def get_raw_schedule(date: date) -> bytes:
    return await _make_request(API_URL, {"actdate": "now", "date": str(date), "apikey": API_KEY})
