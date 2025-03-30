import pytest

from repositories.sqlalchemy_countries_repository import SqlAlchemyCountriesRepository
from schemas.countries import CountryInfo, PartialCountryInfo
from services.countries_service import CountriesService, OperationStatus
from tests import COUNTRY_ALREADY_IN_DB


class TestCountriesService:
    country_not_in_db = CountryInfo(
        code="AAA",
        name="CountryA",
        capital="CapitalA",
        population=1,
    )
    empty_update = PartialCountryInfo()
    non_empty_update = PartialCountryInfo(capital="New capital name")

    @pytest.mark.parametrize(
        "country, expected_result",
        [
            (country_not_in_db, (OperationStatus.CREATE_SUCCESS, "")),
            (
                COUNTRY_ALREADY_IN_DB,
                (
                    OperationStatus.CREATE_FAILURE_ALREADY_EXISTS,
                    "country already exists",
                ),
            ),
        ],
    )
    def test_create_country(self, db_session_test, country, expected_result):
        service = CountriesService(
            repository=SqlAlchemyCountriesRepository(db_session=db_session_test)
        )

        result = service.create_country(country_info=country)

        assert result == expected_result

    @pytest.mark.parametrize(
        "expected_result",
        [
            (OperationStatus.LIST_SUCCESS, [COUNTRY_ALREADY_IN_DB.code]),
        ],
    )
    def test_list_countries(self, db_session_test, expected_result):
        service = CountriesService(
            repository=SqlAlchemyCountriesRepository(db_session=db_session_test)
        )

        result = service.list_countries()

        assert result == expected_result

    @pytest.mark.parametrize(
        "country_code, expected_result",
        [
            (
                COUNTRY_ALREADY_IN_DB.code,
                (OperationStatus.GET_SUCCESS, COUNTRY_ALREADY_IN_DB),
            ),
            (
                country_not_in_db.code,
                (OperationStatus.GET_FAILURE_NOT_FOUND, "country not found"),
            ),
        ],
    )
    def test_get_country(self, db_session_test, country_code, expected_result):
        service = CountriesService(
            repository=SqlAlchemyCountriesRepository(db_session=db_session_test)
        )

        result = service.get_country(country_code)

        assert result == expected_result

    @pytest.mark.parametrize(
        "country_code, country, expected_result",
        [
            (
                COUNTRY_ALREADY_IN_DB.code,
                non_empty_update,
                (OperationStatus.UPDATE_SUCCESS, ""),
            ),
            (
                COUNTRY_ALREADY_IN_DB.code,
                empty_update,
                (OperationStatus.UPDATE_FAILURE_NOTHING_TO_UPDATE, "nothing to update"),
            ),
            (
                country_not_in_db.code,
                non_empty_update,
                (OperationStatus.UPDATE_FAILURE_NOT_FOUND, "country not found"),
            ),
        ],
    )
    def test_update_country(
        self, db_session_test, country_code, country, expected_result
    ):
        service = CountriesService(
            repository=SqlAlchemyCountriesRepository(db_session=db_session_test)
        )

        result = service.update_country(country_code, country)

        assert result == expected_result

    @pytest.mark.parametrize(
        "country_code, expected_result",
        [
            (COUNTRY_ALREADY_IN_DB.code, (OperationStatus.DELETE_SUCCESS, "")),
            (
                country_not_in_db.code,
                (OperationStatus.DELETE_FAILURE_NOT_FOUND, "country not found"),
            ),
        ],
    )
    def test_delete_country(self, db_session_test, country_code, expected_result):
        service = CountriesService(
            repository=SqlAlchemyCountriesRepository(db_session=db_session_test)
        )

        result = service.delete_country(country_code)

        assert result == expected_result
