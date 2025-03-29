from typing import Any

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

from models.dat_country import DatCountry
from repositories.countries_repository import CountriesRepository
from schemas.countries import CountryInfo, PartialCountryInfo


class SqlAlchemyCountriesRepository(CountriesRepository):
    def __init__(self, db_session: Session):
        self._session = db_session

    def bulk_import(self, country_infos: list[dict[str, Any]]) -> int:
        insert_stmt = insert(DatCountry).on_conflict_do_nothing()
        self._session.begin()
        self._session.execute(insert_stmt, country_infos)
        self._session.commit()
        return len(country_infos)

    def create(self, country_info: CountryInfo) -> int:
        raise NotImplementedError()

    def list(self) -> list[str]:
        stmt = select(DatCountry.code).order_by(DatCountry.code)
        result = self._session.execute(stmt).all()
        return [row._mapping["code"] for row in result]

    def get(self, country_code: str) -> CountryInfo | None:
        raise NotImplementedError()

    def update(self, country_code: str, country_info: PartialCountryInfo) -> int:
        raise NotImplementedError()

    def delete(self, country_code: str) -> int:
        raise NotImplementedError()
