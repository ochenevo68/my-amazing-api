from typing import Any

from sqlalchemy import delete, select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from exceptions import CountryAlreadyExistsException
from models.dat_country import DatCountry
from repositories.countries_repository import CountriesRepository
from schemas.countries import CountryInfo


class SqlAlchemyCountriesRepository(CountriesRepository):
    def __init__(self, db_session: Session):
        self._session = db_session

    def bulk_import(self, country_infos: list[dict[str, Any]]) -> int:
        insert_stmt = insert(DatCountry).on_conflict_do_nothing()

        self._session.begin()
        try:
            self._session.execute(insert_stmt, country_infos)
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise e

        return len(country_infos)

    def create(self, country_info: CountryInfo) -> int:
        insert_stmt = insert(DatCountry).values(**country_info.__dict__)

        self._session.begin()
        try:
            result = self._session.execute(insert_stmt)
            inserted_row_count = result.rowcount if result else 0
            if inserted_row_count == 1:
                self._session.commit()
            else:
                self._session.rollback()
        except IntegrityError:
            self._session.rollback()
            raise CountryAlreadyExistsException
        except Exception as e:
            self._session.rollback()
            raise e

        return inserted_row_count

    def list(self) -> list[str]:
        stmt = select(DatCountry.code).order_by(DatCountry.code)
        result = self._session.execute(stmt).all()
        return [row._mapping["code"] for row in result]

    def get(self, country_code: str) -> CountryInfo | None:
        stmt = select(DatCountry).where(DatCountry.code == country_code)
        result = self._session.execute(stmt).scalar()
        return (
            None
            if result is None
            else CountryInfo(
                code=result.code,
                name=result.name,
                capital=result.capital,
                population=result.population,
            )
        )

    def update(self, country_code: str, updates: dict[str, Any]) -> int:
        stmt = (
            update(DatCountry).where(DatCountry.code == country_code).values(**updates)
        )

        self._session.begin()
        try:
            result = self._session.execute(stmt)
            updated_row_count = result.rowcount if result else 0
            if updated_row_count == 1:
                self._session.commit()
            else:
                self._session.rollback()
        except Exception as e:
            self._session.rollback()
            raise e

        return updated_row_count

    def delete(self, country_code: str) -> int:
        delete_stmt = delete(DatCountry).where(DatCountry.code == country_code)

        self._session.begin()
        try:
            result = self._session.execute(delete_stmt)
            deleted_row_count = result.rowcount if result else 0
            if deleted_row_count == 1:
                self._session.commit()
            else:
                self._session.rollback()
        except Exception as e:
            self._session.rollback()
            raise e

        return deleted_row_count
