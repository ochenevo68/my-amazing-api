from typing import Any

import aiohttp

from external import DataSource


class RestcountriesDataSource(DataSource):
    @staticmethod
    async def get_async(session: aiohttp.ClientSession, url: str) -> Any:
        async with session.get(url) as response:
            return await response.json()

    async def get_data(self) -> Any:
        async with aiohttp.ClientSession() as session:
            return await self.get_async(session, "https://restcountries.com/v3.1/all")
