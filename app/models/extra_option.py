# app/models/extra_option.py
from sqlalchemy import Column, Integer, String, Text, DateTime, func, Numeric
from sqlalchemy.orm import relationship
from app.core.database import Base

class ExtraOption(Base):
    __tablename__ = "extra_options"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    price_modifier = Column(Numeric(10, 2), nullable=False) # Renombrado
    description = Column(Text, nullable=True)
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now(), onupdate=func.now())
    delete_at = Column(DateTime, nullable=True)

    products = relationship("ProductExtraOption", back_populates="extra_option")
    order_details = relationship("OrderDetailExtraOption", back_populates="extra_option")