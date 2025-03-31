from abc import ABC, abstractmethod
from typing import Any


class DataSource(ABC):
    """Interface for an external data source."""

    @abstractmethod
    async def get_data(self) -> Any:
        """Get data.

        Returns:
            Data from the source.
        """
        raise NotImplementedError()
