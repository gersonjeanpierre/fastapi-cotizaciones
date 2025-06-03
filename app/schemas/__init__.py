# app/schemas/__init__.py
from .client_type import ClientType, ClientTypeBase, ClientTypeCreate
from .product import Product, ProductBase, ProductCreate
from .product_extra_option import ProductExtraOption, ProductExtraOptionBase, ProductExtraOptionCreate
from .customer import Customer, CustomerBase, CustomerCreate
# Agrega el resto de tus esquemas aquí
# from .store import Store, StoreBase, StoreCreate
# from .order_status import OrderStatus, OrderStatusBase, OrderStatusCreate
# from .order import Order, OrderBase, OrderCreate
# from .order_detail import OrderDetail, OrderDetailBase, OrderDetailCreate

# Para manejar referencias circulares entre modelos Pydantic
# Product.model_rebuild()
# ProductExtraOption.model_rebuild()
# Customer.model_rebuild()
# etc.