from typing import Any

import aiohttp


async def get_async(session: aiohttp.ClientSession, url: str) -> Any:
    async with session.get(url) as response:
        return await response.json()


async def get_data() -> Any:
    async with aiohttp.ClientSession() as session:
        return await get_async(session, "https://restcountries.com/v3.1/all")
