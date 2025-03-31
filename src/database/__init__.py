from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker


class DatabaseConfig:
    """Holds info for connection to database."""

    def __init__(
        self, db_type: str, user: str, password: str, host: str, port: int, db_name: str
    ):
        """Initialize the instance with specified parameters.

        Args:
            db_type: The type of the database. Example: postgresql
            user: The user used when connecting to the database.
            password: The password used when connecting to the database.
            host: The host where the database is.
            port: The port the database server is listening on.
            db_name: The name of the logical database to use.
        """
        self._db_type = db_type
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._db_name = db_name

    def get_url(self) -> str:
        """Get a database connection URL.

        Returns:
            The database connection URL corresponding to the current config
        """
        return f"{self._db_type}://{self._user}:{self._password}@{self._host}:{self._port}/{self._db_name}"


class DatabaseSessionFactory:
    """Utility class responsible for database session creation."""

    def __init__(self, config: DatabaseConfig):
        """Initialize the instance with given DatabaseConfig.

        Args:
            config: The info of the database we want to use.
        """
        engine: Engine = create_engine(
            config.get_url(),
            # echo=True,
        )
        self._session_maker = sessionmaker(bind=engine)

    def get_session(self) -> Session:
        """Get a database session.

        Returns:
            A session in the configured database.
        """
        session_factory = scoped_session(self._session_maker)
        return session_factory()
