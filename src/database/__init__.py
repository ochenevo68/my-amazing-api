from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session


class DatabaseSessionFactory:
    def __init__(self):
        user = "docker"
        password = "docker"
        host = "pj_mdpi_db"
        port = 5432
        db_name = "pj_mdpi"

        engine: Engine = create_engine(
            f"postgresql://{user}:{password}@{host}:{port}/{db_name}",
            # echo=True,
        )

        self._session_maker = sessionmaker(bind=engine)

    def get_session(self) -> Session:
        session_factory = scoped_session(self._session_maker)
        return session_factory()
