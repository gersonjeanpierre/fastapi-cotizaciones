# app/schemas/product.py
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# Forward declaration para evitar circular imports si ExtraOptionInDB o ProductTypeInDB se refieren a Product
# from .extra_option import ExtraOptionInDB
# from .product_type import ProductTypeInDB

class ProductBase(BaseModel):
    sku: str = Field(..., max_length=20)
    name: str = Field(..., max_length=150)
    description: Optional[str] = Field(None, max_length=150)
    unity_measure: str = Field(..., max_length=40)
    price: float = Field(..., gt=0)
    image_url: Optional[str] = Field(None, max_length=150)

class ProductCreate(ProductBase):
    # En la creación, podrías permitir asociar tipos y opciones directamente
    product_type_ids: Optional[List[int]] = None
    extra_option_ids: Optional[List[int]] = None

class ProductUpdate(BaseModel):
    sku: Optional[str] = Field(None, max_length=20)
    name: Optional[str] = Field(None, max_length=150)
    description: Optional[str] = Field(None, max_length=150)
    unity_measure: Optional[str] = Field(None, max_length=40)
    price: Optional[float] = Field(None, gt=0)
    image_url: Optional[str] = Field(None, max_length=150)
    # Para update, se podrían manejar las relaciones por endpoints separados o listas completas de IDs
    # product_type_ids: Optional[List[int]] = None
    # extra_option_ids: Optional[List[int]] = None

class ProductInDB(ProductBase):
    id: int
    create_at: datetime
    update_at: datetime
    delete_at: Optional[datetime] = None

    # Nested relationships will require importing them and avoiding circular deps
    # product_types: List[ProductTypeInDB] = []
    # extra_options: List[ExtraOptionInDB] = []

    model_config = {
        "from_attributes": True
    }

# Schemas para las tablas de unión
class ProductProductTypeBase(BaseModel):
    product_id: int
    product_type_id: int

class ProductProductTypeInDB(ProductProductTypeBase):
    create_at: datetime
    delete_at: Optional[datetime] = None
    model_config = {"from_attributes": True}

class ProductExtraOptionBase(BaseModel):
    product_id: int
    extra_option_id: int

class ProductExtraOptionInDB(ProductExtraOptionBase):
    create_at: datetime
    delete_at: Optional[datetime] = None
    model_config = {"from_attributes": True}