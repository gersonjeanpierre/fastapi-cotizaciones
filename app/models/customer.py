# app/models/customer.py
from sqlalchemy import Column, Integer, String, CHAR, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base # Importa Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    clientTypeId = Column(Integer, ForeignKey("client_types.id"), nullable=False)
    entityType = Column(CHAR(1), nullable=False)
    ruc = Column(CHAR(11), nullable=True)
    dni = Column(CHAR(8), nullable=True)
    name = Column(String(35), nullable=True)
    lastName = Column(String(40), nullable=True)
    businessName = Column(String(150), nullable=True)
    phoneNumber = Column(String(15), nullable=True)
    email = Column(String(60), nullable=True)
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

    orders = relationship("Order", back_populates="customer")
    client_type = relationship("ClientType", back_populates="customers")