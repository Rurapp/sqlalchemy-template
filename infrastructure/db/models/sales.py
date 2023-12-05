from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from infrastructure.db.models.base_model import Base


class Sales(Base):
    __tablename__ = 'sales_table'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(), default=datetime.now())
    user_id = Column(Integer, ForeignKey('user_table.id'), nullable=False)
    price = Column(Integer)

    def __init__(self, user_id, price):
        self.user_id = user_id
        self.price = price
