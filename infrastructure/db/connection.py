import psycopg2
import alembic.config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from application import settings
from infrastructure.db.models.base_model import Base
from infrastructure.db.models.sales import Sales
from infrastructure.db.models.user import User


class DatabaseConnection:
    engine = None
    session = None
    db_username = settings.DB_USERNAME
    db_password = settings.DB_PASSWORD
    db_host = settings.DB_HOST
    db_port = settings.DB_PORT
    db_database = settings.DB_DATABASE

    @classmethod
    def initialize_db(cls):
        cls.start_engine()
        Base.metadata.create_all(cls.engine)

    @classmethod
    def get_session(cls):
        if not cls.session:
            cls.start_engine()
        return cls.session()

    @classmethod
    def start_engine(cls):
        cls.engine = create_engine(cls.get_db_url(), pool_size=10, max_overflow=0, pool_pre_ping=True)
        cls.session = sessionmaker(bind=cls.engine)

    @classmethod
    def get_db_connection(cls):
        return psycopg2.connect(cls.get_db_url())

    @classmethod
    def get_db_url(cls):
        return "postgresql://{}:{}@{}:{}/{}".format(
            cls.db_username,
            cls.db_password,
            cls.db_host,
            cls.db_port,
            cls.db_database,
        )
