from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.session import Base

class Crypto(Base):
    __tablename__ = "cryptos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    symbol = Column(String, index=True, unique=True)
    price = Column(Float)
    market_cap = Column(Float)
    last_updated = Column(DateTime, default=datetime.utcnow)
