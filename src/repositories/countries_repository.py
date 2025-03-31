from abc import ABC, abstractmethod
from typing import Any

from schemas.countries import CountryInfo


class CountriesRepository(ABC):
    """Interface of a CountriesRepository."""

    @abstractmethod
    def bulk_import(self, country_infos: list[dict[str, Any]]) -> int:
        """Import given country infos into the database in one go.

        Args:
            country_infos: The country infos to import.

        Returns:
            The number of records imported.
        """
        raise NotImplementedError()

    @abstractmethod
    def create(self, country_info: CountryInfo) -> int:
        """Insert given country info into the database.

        Args:
            country_info: The country info to insert.

        Returns:
            The inserted row count.
        """
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> list[str]:
        """List the country code of all countries in the database.

        Returns:
            The country code of all countries currently in the database.
        """
        raise NotImplementedError()

    @abstractmethod
    def get(self, country_code: str) -> CountryInfo | None:
        """Get all we know about a specific country.

        Args:
            country_code: The code of the country.

        Returns:
            All the info about the country. None if it does not exist.
        """
        raise NotImplementedError()

    @abstractmethod
    def update(self, country_code: str, country_info: dict[str, Any]) -> int:
        """Update the info about a country.

        Args:
            country_code: The code of the country to update.
            country_info: The new values of the fields to update.

        Returns:
            The updated row count. (1 in case of success, 0 if the country was not found)
        """
        raise NotImplementedError()

    @abstractmethod
    def delete(self, country_code: str) -> int:
        """Delete the country with given code.

        Args:
            country_code: The code of the country to delete.

        Returns:
            The deleted row count. (1 in case of success, 0 if the country was not found)
        """
        raise NotImplementedError()
