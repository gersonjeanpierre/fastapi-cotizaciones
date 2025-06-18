# src/models/customer.py
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from src.core.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    type_client_id = Column(Integer, ForeignKey("type_clients.id"), nullable=False)
    entity_type = Column(CHAR(1), nullable=False) # 'N' o 'J'
    ruc = Column(String(11), unique=True, index=True, nullable=True) # Puede ser nulo, pero único si existe
    dni = Column(String(8), unique=True, index=True, nullable=True)   # Puede ser nulo, pero único si existe
    name = Column(String(35), nullable=True) # Solo para persona natural
    last_name = Column(String(40), nullable=True) # Solo para persona natural
    business_name = Column(String(150), nullable=True) # Solo para persona jurídica
    phone_number = Column(String(15), nullable=True)
    email = Column(String(100), unique=True, index=True, nullable=False) # Email siempre requerido y único
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now(), onupdate=func.now())
    delete_at = Column(DateTime, nullable=True)

    type_client = relationship("TypeClient", back_populates="customers")
    orders = relationship("Order", back_populates="customer") # Relación con Orders