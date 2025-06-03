# app/models/order.py
from sqlalchemy import Column, Integer, DECIMAL, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    store_id = Column(Integer, ForeignKey("store.id"), nullable=False)
    order_status_id = Column(Integer, ForeignKey("order_statuses.id"), nullable=True)
    total_amount = Column(DECIMAL(10, 2), nullable=False)
    description = Column(String(150), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    customer = relationship("Customer", back_populates="orders")
    store = relationship("Store", back_populates="orders")
    status = relationship("OrderStatus", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")