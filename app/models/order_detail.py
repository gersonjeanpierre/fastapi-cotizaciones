# app/models/order_detail.py
from sqlalchemy import Column, Integer, SmallInteger, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_extra_option_id = Column(Integer, ForeignKey("product_extra_options.id"), nullable=False)
    quantity = Column(SmallInteger, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    product = relationship("Product", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")
    product_extra_option = relationship("ProductExtraOption", back_populates="order_details")