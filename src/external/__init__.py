from abc import ABC, abstractmethod
from typing import Any


class DataSource(ABC):
    @abstractmethod
    async def get_data(self) -> Any:
        raise NotImplementedError()
