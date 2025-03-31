from typing import Any, Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from database import DatabaseConfig, DatabaseSessionFactory
from external import DataSource
from external.restcountries import RestcountriesDataSource
from repositories.countries_repository import CountriesRepository
from repositories.sqlalchemy_countries_repository import SqlAlchemyCountriesRepository


def get_db_session() -> Generator[Session, Any, None]:
    """Get a database session to the API's database.

    Returns:
        A session to the database.
    """
    session_factory = DatabaseSessionFactory(DatabaseConfig())
    session = session_factory.get_session()
    try:
        yield session
    finally:
        session.close()


def get_countries_repository(
    db_session: Session = Depends(get_db_session),
) -> CountriesRepository:
    """Get a CountriesRepository.

    Args:
        db_session: Injected database session dependency.

    Returns:
        A CountriesRepository.
    """
    return SqlAlchemyCountriesRepository(db_session=db_session)


def get_data_source() -> DataSource:
    """Get a DataSource.

    Returns:
        A DataSource.
    """
    return RestcountriesDataSource()
