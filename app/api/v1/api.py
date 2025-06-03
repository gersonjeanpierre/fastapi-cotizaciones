# app/api/v1/api.py
from fastapi import APIRouter
from .endpoints import customer # Importa el router de customer

api_router = APIRouter()
api_router.include_router(customer.router)
# Agrega otros routers de endpoints aquí:
# api_router.include_router(product.router)
# etc.