# app/schemas/product.py
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

class ProductBase(BaseModel):
    name: str
    base_price_final: Decimal
    base_price_printer: Decimal
    image: Optional[str] = None
    thumbnail: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # Si quieres incluir opciones extras al leer un producto, descomenta:
    # product_extra_options: List["ProductExtraOption"] = []

    class Config:
        from_attributes = True

# Para referencias circulares en Pydantic si ProductExtraOption se importa aquí
# Product.model_rebuild()