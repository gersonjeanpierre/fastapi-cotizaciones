# app/models/product.py
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base # Importa Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    base_price_final = Column(DECIMAL(8, 2), nullable=False)
    base_price_printer = Column(DECIMAL(8, 2), nullable=False)
    image = Column(String(150), nullable=True)
    thumbnail = Column(String(150), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    product_extra_options = relationship("ProductExtraOption", back_populates="product")
    order_details = relationship("OrderDetail", back_populates="product")