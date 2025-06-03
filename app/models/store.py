# app/models/store.py
from sqlalchemy import Column, Integer, String, CHAR, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Store(Base):
    __tablename__ = "store"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(CHAR(8), nullable=False)
    description = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    orders = relationship("Order", back_populates="store")