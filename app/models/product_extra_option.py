# app/models/product_extra_option.py
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base # Importa Base

class ProductExtraOption(Base):
    __tablename__ = "product_extra_options"

    id = Column(Integer, primary_key=True, index=True)
    productId = Column(Integer, ForeignKey("products.id"), nullable=False)
    description = Column(String(150), nullable=False)
    baseCost = Column(DECIMAL(8, 2), nullable=False)
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

    product = relationship("Product", back_populates="product_extra_options")
    order_details = relationship("OrderDetail", back_populates="product_extra_option")