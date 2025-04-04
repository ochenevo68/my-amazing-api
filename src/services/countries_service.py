from enum import Enum, auto

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
    """Service responsible for manipulating countries."""

    def __init__(self, repository: CountriesRepository):
        """Initialize the instance with a CountriesRepository.

        Args:
            repository: The CountriesRepository to use for countries manipulation.
        """
        self._repository = repository

    def create_country(self, country_info: CountryInfo) -> tuple[OperationStatus, str]:
        """Create a country with given info.

        Args:
            country_info: The info about the country to create.

        Returns:
            The operation status (success/failure), and some detail.
            Example: (CREATE_FAILURE, "failed to create country for some reason")
        """
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
        """List all countries we know of.

        Returns:
            The operation status (success/failure), and some detail.
            Example: (LIST_SUCCESS, ["AAA", ...])
        """
        try:
            detail = self._repository.list()
        except Exception:
            detail = []
        return OperationStatus.LIST_SUCCESS, detail

    def get_country(
        self, country_code: str
    ) -> tuple[OperationStatus, CountryInfo | str]:
        """Get info about a country.

        Args:
            country_code: The code of the country.

        Returns:
            The operation status (success/failure), and some detail.
            Example: (GET_FAILURE_NOT_FOUND, "country not found")
        """
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
        """Update some info about a country.

        Args:
            country_code: The code of the country.
            country_info: The new info.

        Returns:
            The operation status (success/failure), and some detail.
            Example: (UPDATE_FAILURE_NOTHING_TO_UPDATE, "nothing to update")
        """
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
        """Delete a country.

        Args:
            country_code: The code of the country.

        Returns:
            The operation status (success/failure), and some detail.
            Example: (DELETE_FAILURE_NOT_FOUND, "country not found")
        """
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
