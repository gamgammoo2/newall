from sqlalchemy import Column,Text
from sqlalchemy.orm import relationship

from .database import Base


class Stock(Base):
    __tablename__ = "stock"

    Code = Column(Text, index=True)
    Name = Column(String(20), index=True)
    MarketId = Column(String(100), index=True)
    Dept = Column(Boolean, index=True)
    Close = Column(Text, index=True)