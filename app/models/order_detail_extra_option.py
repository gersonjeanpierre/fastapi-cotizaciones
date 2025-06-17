# app/models/order_detail_extra_option.py
from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class OrderDetailExtraOption(Base):
    __tablename__ = "order_detail_extra_options"

    order_detail_id = Column(Integer, ForeignKey("order_details.id"), primary_key=True)
    extra_option_id = Column(Integer, ForeignKey("extra_options.id"), primary_key=True)
    price_at_order = Column(Numeric(10, 2), nullable=False) # Precio de la opción en el momento del pedido

    order_detail = relationship("OrderDetail", back_populates="extra_options_details")
    extra_option = relationship("ExtraOption", back_populates="order_details")