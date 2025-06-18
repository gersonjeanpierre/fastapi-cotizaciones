# src/models/product_type.py
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship
from src.core.database import Base

class ProductType(Base):
    __tablename__ = "product_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    create_at = Column(DateTime, default=func.now())
    delete_at = Column(DateTime, nullable=True)

    products = relationship("ProductProductType", back_populates="product_type")