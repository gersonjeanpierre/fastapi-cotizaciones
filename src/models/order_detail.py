# src/models/order_detail.py
from sqlalchemy import Column, Integer, String, DateTime, func, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from src.core.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False) # Precio del producto en el momento de la compra
    total_extra_options = Column(Numeric(10, 2), default=0.00, nullable=False) # Suma de price_modifier de las extra_options
    subtotal = Column(Numeric(10, 2), nullable=False) # quantity * (unit_price + total_extra_options)
    create_at = Column(DateTime, default=func.now())
    delete_at = Column(DateTime, nullable=True)

    order = relationship("Order", back_populates="order_details")
    product = relationship("Product", back_populates="order_details")
    extra_options_details = relationship("OrderDetailExtraOption", back_populates="order_detail")