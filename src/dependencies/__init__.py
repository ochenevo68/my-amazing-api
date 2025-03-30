from fastapi import Depends
from sqlalchemy.orm import Session

from database import DatabaseConfig, DatabaseSessionFactory
from external import RestcountriesDataSource
from repositories.sqlalchemy_countries_repository import SqlAlchemyCountriesRepository


def get_db_session():
    session_factory = DatabaseSessionFactory(
        DatabaseConfig(
            db_type="postgresql",
            user="docker",
            password="docker",
            host="pj_mdpi_db",
            port=5432,
            db_name="pj_mdpi",
        )
    )
    session = session_factory.get_session()
    try:
        yield session
    finally:
        session.close()


def get_countries_repository(db_session: Session = Depends(get_db_session)):
    return SqlAlchemyCountriesRepository(db_session=db_session)


def get_data_source():
    return RestcountriesDataSource()
