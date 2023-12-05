from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from infrastructure.db.models.base_model import Base


class User(Base):
    __tablename__ = 'user_table'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(), default=datetime.now())
    name = Column(String, nullable=False)
    cedula = Column(Integer, unique=True)

    def __init__(self, name, cedula):
        self.name = name
        self.cedula = cedula
