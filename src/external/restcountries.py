from typing import Any

import aiohttp
from tenacity import retry, stop_after_attempt, wait_fixed
from typing_extensions import override

from external import DataSource


class RestcountriesDataSource(DataSource):
    """DataSource for the online restcountries.com API."""

    @staticmethod
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_fixed(3),
        reraise=True,
    )
    async def _get_async(session: aiohttp.ClientSession, url: str) -> Any:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
        raise TimeoutError()

    @override
    async def get_data(self) -> Any:
        async with aiohttp.ClientSession() as session:
            return await self._get_async(session, "https://restcountries.com/v3.1/all")
