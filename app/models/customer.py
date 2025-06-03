# app/models/customer.py
from sqlalchemy import Column, Integer, String, CHAR, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base # Importa Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    entity_type = Column(CHAR(1), nullable=False)
    ruc = Column(CHAR(11), nullable=True)
    dni = Column(CHAR(8), nullable=True)
    name = Column(String(35), nullable=True)
    last_name = Column(String(40), nullable=True)
    business_name = Column(String(150), nullable=True)
    phone_number = Column(String(15), nullable=True)
    email = Column(String(60), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    orders = relationship("Order", back_populates="customer")