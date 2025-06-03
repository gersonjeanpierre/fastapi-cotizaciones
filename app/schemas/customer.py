# app/schemas/customer.py
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CustomerBase(BaseModel):
    entity_type: str
    ruc: Optional[str] = None
    dni: Optional[str] = None
    name: Optional[str] = None
    last_name: Optional[str] = None
    business_name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # Si quieres incluir las órdenes de un cliente:
    # orders: List["Order"] = []

    class Config:
        from_attributes = True

# Customer.model_rebuild()