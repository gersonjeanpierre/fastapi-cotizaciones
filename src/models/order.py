# src/models/order.py
from sqlalchemy import Column, Integer, String, DateTime, func, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from src.core.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    store_id = Column(Integer, ForeignKey("stores.id"), nullable=False)
    order_status_id = Column(Integer, ForeignKey("order_status.id"), nullable=False)
    order_date = Column(DateTime, nullable=False, default=func.now())
    total_amount = Column(Numeric(10, 2), nullable=False) # Suma de subtotales de order_details
    profit_margin = Column(Numeric(10, 2), nullable=False) # Margen de ganancia
    discount_srclied = Column(Numeric(10, 2), default=0.00, nullable=False)
    final_amount = Column(Numeric(10, 2), nullable=False) # Monto final a pagar (con IGV si aplica)
    payment_method = Column(String(50), nullable=True)
    shipping_address = Column(String(200), nullable=True)
    notes = Column(String(200), nullable=True)
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now(), onupdate=func.now())
    delete_at = Column(DateTime, nullable=True)

    customer = relationship("Customer", back_populates="orders")
    store = relationship("Store", back_populates="orders")
    status = relationship("OrderStatus", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")