# app/models/client_type.py
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base # Importa Base desde la nueva ubicación

class ClientType(Base):
    __tablename__ = "client_types"

    id = Column(Integer, primary_key=True, index=True)
    typeName = Column(String(40), unique=True, nullable=False)
    profitMargin = Column(DECIMAL(2, 2), nullable=False)
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

    customers = relationship("Customer", back_populates="client_type")