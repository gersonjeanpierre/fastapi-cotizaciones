# app/schemas/product_extra_option.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class ProductExtraOptionBase(BaseModel):
    product_id: int
    description: str
    base_price_final: Decimal
    base_price_printer: Decimal

class ProductExtraOptionCreate(ProductExtraOptionBase):
    pass

class ProductExtraOption(ProductExtraOptionBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # Si quieres incluir el producto al leer una opción extra:
    # product: Optional["Product"] = None

    class Config:
        from_attributes = True

# ProductExtraOption.model_rebuild()