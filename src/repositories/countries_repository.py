from abc import ABC, abstractmethod
from typing import Any

from schemas.countries import CountryInfo


class CountriesRepository(ABC):
    @abstractmethod
    def bulk_import(self, country_infos: list[dict[str, Any]]) -> int:
        raise NotImplementedError()

    @abstractmethod
    def create(self, country_info: CountryInfo) -> int:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> list[str]:
        raise NotImplementedError()

    @abstractmethod
    def get(self, country_code: str) -> CountryInfo | None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, country_code: str, country_info: dict[str, Any]) -> int:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, country_code: str) -> int:
        raise NotImplementedError()
