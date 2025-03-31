from typing import Any

import aiohttp
from typing_extensions import override

from external import DataSource


class RestcountriesDataSource(DataSource):
    """DataSource for the online restcountries.com API."""

    @staticmethod
    async def _get_async(session: aiohttp.ClientSession, url: str) -> Any:
        async with session.get(url) as response:
            return await response.json()

    @override
    async def get_data(self) -> Any:
        async with aiohttp.ClientSession() as session:
            return await self._get_async(session, "https://restcountries.com/v3.1/all")
