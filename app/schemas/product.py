from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

class ProductBase(BaseModel):
    name: str
    type: str
    unityMeasure: str
    baseCost: Decimal    
    imageUrl: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

    # Si quieres cargar las opciones extra junto con el producto,
    # descomenta la siguiente línea y asegúrate de importar ProductExtraOption
    # from .product_extra_option import ProductExtraOption # Importación relativa
    # product_extra_options: List[ProductExtraOption] = []

    class Config:
        from_attributes = True

# Si hay referencias circulares (ej. ProductExtraOption referencia a Product y viceversa),
# podrías necesitar esta línea después de todas las definiciones de modelos en el archivo
# Product.model_rebuild()