from sqlalchemy import Column, Integer, String, Float, Date
from app.db.base import Base

#database model
class Domain(Base):
    __tablename__ = "domains"

    user_id = Column(Integer,nullable=False)
    id = Column(Integer, primary_key=True, index=True)
    domain_name = Column(String(100),nullable=False)
    buy_price = Column(Float, nullable=False)
    buy_date = Column(Date, nullable=False)