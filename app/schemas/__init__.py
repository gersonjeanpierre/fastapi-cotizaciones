# app/schemas/__init__.py
from .customer import (
    CustomerCreate,
    CustomerUpdate,
    CustomerInDB,
)
from .store import (
    StoreCreate,
    StoreUpdate,
    StoreInDB,
)
from .order import (
    OrderCreate,
    OrderUpdate,
    OrderInDB,
    OrderDetailCreate,
    OrderDetailInDB,
    OrderDetailExtraOptionInDB,
)
from .product import (
    ProductCreate,
    ProductUpdate,
    ProductInDB,
    ProductExtraOptionInDB,
)
from .extra_option import (
    ExtraOptionCreate,
    ExtraOptionUpdate,
    ExtraOptionInDB,
)
from .order_status import (
    OrderStatusCreate,
    OrderStatusUpdate,
    OrderStatusInDB,
)
from .type_client import (
    TypeClientCreate,
    TypeClientUpdate,
    TypeClientInDB,
)
from .product_type import (
    ProductTypeCreate,
    ProductTypeUpdate,
    ProductTypeInDB,
)

