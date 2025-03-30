from enum import Enum, auto
from typing import Optional

from exceptions import CountryAlreadyExistsException
from repositories.countries_repository import CountriesRepository
from schemas.countries import CountryInfo, PartialCountryInfo


class OperationStatus(Enum):
    CREATE_SUCCESS = auto()
    CREATE_FAILURE = auto()
    CREATE_FAILURE_ALREADY_EXISTS = auto()
    LIST_SUCCESS = auto()
    GET_SUCCESS = auto()
    GET_FAILURE = auto()
    GET_FAILURE_NOT_FOUND = auto()
    UPDATE_SUCCESS = auto()
    UPDATE_FAILURE = auto()
    UPDATE_FAILURE_NOT_FOUND = auto()
    UPDATE_FAILURE_NOTHING_TO_UPDATE = auto()
    DELETE_SUCCESS = auto()
    DELETE_FAILURE = auto()
    DELETE_FAILURE_NOT_FOUND = auto()


class CountriesService:
    def __init__(self, repository: CountriesRepository):
        self._repository = repository

    def create_country(self, country_info: CountryInfo) -> tuple[OperationStatus, str]:
        status = OperationStatus.CREATE_FAILURE
        detail = "failed to create country for some reason"
        try:
            inserted_count = self._repository.create(country_info)
            if inserted_count == 1:
                status = OperationStatus.CREATE_SUCCESS
                detail = ""
        except CountryAlreadyExistsException as e:
            status = OperationStatus.CREATE_FAILURE_ALREADY_EXISTS
            detail = e.message
        return status, detail

    def list_countries(self) -> tuple[OperationStatus, list[str]]:
        try:
            detail = self._repository.list()
        except Exception:
            detail = []
        return OperationStatus.LIST_SUCCESS, detail

    def get_country(
        self, country_code: str
    ) -> tuple[OperationStatus, CountryInfo | str]:
        country = self._repository.get(country_code)
        status, detail = (
            (OperationStatus.GET_SUCCESS, country)
            if country
            else (
                OperationStatus.GET_FAILURE_NOT_FOUND,
                "country not found",
            )
        )

        return status, detail

    def update_country(
        self, country_code: str, country_info: PartialCountryInfo
    ) -> tuple[OperationStatus, str]:
        updates = {k: v for k, v in country_info.__dict__.items() if v is not None}
        if len(updates) == 0:  # Nothing to update, NOOP
            return OperationStatus.UPDATE_FAILURE_NOTHING_TO_UPDATE, "nothing to update"

        status = OperationStatus.UPDATE_FAILURE
        detail = "failed to update country for some reason"

        updated_count = self._repository.update(country_code, updates)
        if updated_count == 1:
            status = OperationStatus.UPDATE_SUCCESS
            detail = ""
        elif updated_count == 0:
            status = OperationStatus.UPDATE_FAILURE_NOT_FOUND
            detail = "country not found"

        return status, detail

    def delete_country(self, country_code: str) -> tuple[OperationStatus, str]:
        status = OperationStatus.DELETE_FAILURE
        detail = "failed to delete country for some reason"

        deleted_count = self._repository.delete(country_code)
        if deleted_count == 1:
            status = OperationStatus.DELETE_SUCCESS
            detail = ""
        elif deleted_count == 0:
            status = OperationStatus.DELETE_FAILURE_NOT_FOUND
            detail = "country not found"

        return status, detail
