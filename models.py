from sqlalchemy import create_engine, Column, Integer, String, Text, DECIMAL, SmallInteger, DateTime, CHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

from database import Base
# --- Definición de Modelos SQLAlchemy ---

# Modelo para client_types
class ClientType(Base):
    __tablename__ = "client_types" # Nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True) # index=True para que SQLAlchemy cree un índice
    type_name = Column(String(40), unique=True, nullable=False)
    profit_margin = Column(DECIMAL(2, 2), nullable=False) # decimal(2,2)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relaciones (ej. si Customer o Order tuviera un client_type_id)
    # customers = relationship("Customer", back_populates="client_type")

# Modelo para products
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    base_price_final = Column(DECIMAL(8, 2), nullable=False)
    base_price_printer = Column(DECIMAL(8, 2), nullable=False)
    image = Column(String(150), nullable=True)
    thumbnail = Column(String(150), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relaciones
    product_extra_options = relationship("ProductExtraOption", back_populates="product")
    order_details = relationship("OrderDetail", back_populates="product")

# Modelo para product_extra_options
class ProductExtraOption(Base):
    __tablename__ = "product_extra_options"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    description = Column(String(150), nullable=False)
    base_price_final = Column(DECIMAL(8, 2), nullable=False)
    base_price_printer = Column(DECIMAL(8, 2), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relaciones
    product = relationship("Product", back_populates="product_extra_options")
    order_details = relationship("OrderDetail", back_populates="product_extra_option")

# Modelo para customers
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    entity_type = Column(CHAR(1), nullable=False) # char(1)
    ruc = Column(CHAR(11), nullable=True) # char(11)
    dni = Column(CHAR(8), nullable=True) # char(8)
    name = Column(String(35), nullable=True)
    last_name = Column(String(40), nullable=True)
    business_name = Column(String(150), nullable=True)
    phone_number = Column(String(15), nullable=True)
    email = Column(String(60), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relaciones
    orders = relationship("Order", back_populates="customer")

# Modelo para store
class Store(Base):
    __tablename__ = "store"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(CHAR(8), nullable=False)
    description = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relaciones
    orders = relationship("Order", back_populates="store")

# Modelo para order_statuses
class OrderStatus(Base):
    __tablename__ = "order_statuses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relaciones
    orders = relationship("Order", back_populates="status")


# Modelo para orders
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    store_id = Column(Integer, ForeignKey("store.id"), nullable=False)
    order_status_id = Column(Integer, ForeignKey("order_statuses.id"), nullable=True) # Puede ser nullable o con default
    total_amount = Column(DECIMAL(10, 2), nullable=False) # Asumo 10,2 como antes
    description = Column(String(150), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relaciones
    customer = relationship("Customer", back_populates="orders")
    store = relationship("Store", back_populates="orders")
    status = relationship("OrderStatus", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")

# Modelo para order_details
class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_extra_option_id = Column(Integer, ForeignKey("product_extra_options.id"), nullable=False)
    quantity = Column(SmallInteger, nullable=False) # smallint
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relaciones
    product = relationship("Product", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")
    product_extra_option = relationship("ProductExtraOption", back_populates="order_details")