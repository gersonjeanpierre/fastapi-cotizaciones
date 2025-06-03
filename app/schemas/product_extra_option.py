from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

# Importa el esquema Product si quieres incluir el producto al leer una opción extra
# from .product import Product

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

    # Si quieres cargar el objeto Product relacionado al leer una ProductExtraOption,
    # descomenta la siguiente línea.
    # product: Optional[Product] = None # Ten en cuenta las referencias circulares

    class Config:
        from_attributes = True

# Si hay referencias circulares (ej. ProductExtraOption referencia a Product y viceversa),
# podrías necesitar esta línea después de todas las definiciones de modelos en el archivo
# ProductExtraOption.model_rebuild()