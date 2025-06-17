# app/models/store.py
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10), unique=True, nullable=True) # Puede ser nulo, pero único si existe
    name = Column(String(100), nullable=False)
    address = Column(String(255), nullable=True)
    phone_number = Column(String(15), nullable=True)
    email = Column(String(100), nullable=True)
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now(), onupdate=func.now())
    delete_at = Column(DateTime, nullable=True)

    orders = relationship("Order", back_populates="store")