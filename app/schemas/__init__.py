# app/schemas/__init__.py
from .client_type import ClientType, ClientTypeBase, ClientTypeCreate
from .product import Product, ProductBase, ProductCreate
from .product_extra_option import ProductExtraOption, ProductExtraOptionBase, ProductExtraOptionCreate
from .customer import Customer, CustomerBase, CustomerCreate
from .store import Store, StoreBase, StoreCreate
from .order_status import OrderStatus, OrderStatusBase, OrderStatusCreate 



# Para manejar referencias circulares entre modelos Pydantic
# Product.model_rebuild()
# ProductExtraOption.model_rebuild()
# Customer.model_rebuild()
# etc.