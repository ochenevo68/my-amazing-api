import pytest

from repositories.sqlalchemy_countries_repository import SqlAlchemyCountriesRepository
from services.import_service import ImportService
from tests import RestcountriesMockDataSource


class TestImportService:
    @pytest.mark.parametrize(
        "expected_result",
        [3],
    )
    async def test_import_data(self, db_session_test, expected_result):
        service = ImportService(
            repository=SqlAlchemyCountriesRepository(db_session=db_session_test),
            data_source=RestcountriesMockDataSource(),
        )

        result = await service.import_data()

        assert result == expected_result
