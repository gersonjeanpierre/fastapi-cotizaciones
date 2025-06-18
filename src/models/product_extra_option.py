from sqlalchemy import Column, DateTime, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from src.core.database import Base

class ProductExtraOption(Base):
    __tablename__ = 'product_extra_options'

    product_id = Column(Integer, ForeignKey("products.id"), primary_key=True)
    extra_option_id = Column(Integer, ForeignKey("extra_options.id"), primary_key=True)
    create_at = Column(DateTime, default=func.now())
    delete_at = Column(DateTime, nullable=True)

    product = relationship("Product", back_populates="extra_options")
    extra_option = relationship("ExtraOption", back_populates="products")