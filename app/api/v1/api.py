# app/api/v1/api.py
from fastapi import APIRouter
from .endpoints import customer
from .endpoints import product
from .endpoints import store
from .endpoints import order_status
from .endpoints import product_extra_option

api_router = APIRouter()
api_router.include_router(customer.router)
api_router.include_router(product.router)
api_router.include_router(store.router)
api_router.include_router(order_status.router)
api_router.include_router(product_extra_option.router)
# Agrega otros routers de endpoints aquí:
# api_router.include_router(product.router)
# etc.