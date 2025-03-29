from fastapi import Depends
from sqlalchemy.orm import Session

from database import DatabaseSessionFactory
from repositories.sqlalchemy_countries_repository import SqlAlchemyCountriesRepository


def get_db_session():
    session_factory = DatabaseSessionFactory()
    session = session_factory.get_session()
    try:
        yield session
    finally:
        session.close()


def get_countries_repository(db_session: Session = Depends(get_db_session)):
    return SqlAlchemyCountriesRepository(db_session=db_session)
