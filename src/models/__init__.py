# src/models/__init__.py
# Importa todos los modelos para que Base.metadata.create_all() los detecte
from .customer import Customer
from .extra_option import ExtraOption
from .order_detail_extra_option import OrderDetailExtraOption
from .order_detail import OrderDetail
from .order_status import OrderStatus
from .order import Order
from .product_product_type import ProductProductType
from .product_type import ProductType
from .product_extra_option import ProductExtraOption
from .product import Product
from .store import Store
from .type_client import TypeClient

# Si quisieras exportar Base desde aquí, lo harías así:
from src.core.database import Base