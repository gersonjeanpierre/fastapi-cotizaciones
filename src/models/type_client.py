# src/models/type_client.py (renombrado para reflejar el nombre de la tabla)
from sqlalchemy import Column, Integer, String, DateTime, func, Numeric
from sqlalchemy.orm import relationship
from src.core.database import Base

class TypeClient(Base):
    __tablename__ = "type_clients" # Nombre de tu tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10), unique=True, nullable=False) # Ampliado a varchar(10)
    name = Column(String(50), unique=True, nullable=False)
    margin = Column(Numeric(3, 2), nullable=False) # Decimal(3,2) para (ej. 0.05)
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now(), onupdate=func.now())
    delete_at = Column(DateTime, nullable=True)

    customers = relationship("Customer", back_populates="type_client") # Relación con Customers