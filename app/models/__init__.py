# app/models/__init__.py
# Importa todos los modelos para que Base.metadata.create_all() los detecte
from .client_type import ClientType
from .product import Product
from .product_extra_option import ProductExtraOption
from .customer import Customer
from .store import Store
from .order_status import OrderStatus
from .order import Order
from .order_detail import OrderDetail

# Si quisieras exportar Base desde aquí, lo harías así:
from app.core.database import Base