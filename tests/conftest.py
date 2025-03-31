import pytest
from sqlalchemy import insert, text
from sqlalchemy.orm import Session

from database import DatabaseConfig, DatabaseSessionFactory
from models.dat_country import DatCountry
from tests import COUNTRY_ALREADY_IN_DB


def reset_db(session: Session):
    session.execute(text("TRUNCATE TABLE dat_country"))
    session.execute(insert(DatCountry).values(**COUNTRY_ALREADY_IN_DB.__dict__))
    session.commit()


@pytest.fixture(scope="function")
def db_session_test():
    session_factory = DatabaseSessionFactory(
        DatabaseConfig(
            host="pj_mdpi_db_test",
        )
    )
    session = session_factory.get_session()
    reset_db(session)
    try:
        yield session
    finally:
        session.close()
