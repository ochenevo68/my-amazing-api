from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker


class DatabaseConfig:
    def __init__(
        self, db_type: str, user: str, password: str, host: str, port: int, db_name: str
    ):
        self._db_type = db_type
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._db_name = db_name

    def get_url(self):
        return f"{self._db_type}://{self._user}:{self._password}@{self._host}:{self._port}/{self._db_name}"


class DatabaseSessionFactory:
    def __init__(self, config: DatabaseConfig):
        engine: Engine = create_engine(
            config.get_url(),
            # echo=True,
        )
        self._session_maker = sessionmaker(bind=engine)

    def get_session(self) -> Session:
        session_factory = scoped_session(self._session_maker)
        return session_factory()
