# src/models/product.py
from sqlalchemy import Column, Integer, String, DateTime, func, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from src.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(20), unique=True, nullable=False)
    name = Column(String(150), nullable=False)
    description = Column(String(150), nullable=True)
    unity_measure = Column(String(40), nullable=False)
    price = Column(Numeric(10, 2), nullable=False) # Precio base del producto
    image_url = Column(String(150), nullable=True)
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now(), onupdate=func.now())
    delete_at = Column(DateTime, nullable=True)

    # Relaciones con tablas de unión y otras
    product_types = relationship("ProductProductType", back_populates="product")
    extra_options = relationship("ProductExtraOption", back_populates="product")

    order_details = relationship("OrderDetail", back_populates="product")