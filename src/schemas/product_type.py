# app/schemas/product_type.py
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ProductTypeBase(BaseModel):
    name: str = Field(..., max_length=100 )
    description: Optional[str] = Field(None )

class ProductTypeCreate(ProductTypeBase):
    pass

class ProductTypeUpdate(BaseModel):
    name: Optional[str] = Field(..., max_length=100)
    description: Optional[str] = None

class ProductTypeInDB(ProductTypeBase):
    id: int
    create_at: datetime
    delete_at: Optional[datetime] = None

    model_config = {
        "from_attributes": True
    }