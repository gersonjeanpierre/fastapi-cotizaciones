# app/models/product_product_type.py
from sqlalchemy import Column, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class ProductProductType(Base):
    __tablename__ = "product_product_types"

    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    product_type_id = Column(Integer, ForeignKey("product_types.id"), primary_key=True)
    create_at = Column(DateTime, default=func.now())
    delete_at = Column(DateTime, nullable=True)

    product = relationship("Product", back_populates="product_types")
    product_type = relationship("ProductType", back_populates="products")