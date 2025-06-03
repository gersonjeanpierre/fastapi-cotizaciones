# app/models/client_type.py
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime
from sqlalchemy.sql import func
from app.core.database import Base # Importa Base desde la nueva ubicación

class ClientType(Base):
    __tablename__ = "client_types"

    id = Column(Integer, primary_key=True, index=True)
    type_name = Column(String(40), unique=True, nullable=False)
    profit_margin = Column(DECIMAL(2, 2), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())