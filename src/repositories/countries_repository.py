from abc import ABC, abstractmethod
from typing import Any

from schemas.countries import CountryInfo, PartialCountryInfo


class CountriesRepository(ABC):
    @abstractmethod
    def bulk_import(self, country_infos: list[dict[str, Any]]) -> int:
        pass

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
    def update(self, country_code: str, country_info: PartialCountryInfo) -> int:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, country_code: str) -> int:
        raise NotImplementedError()
