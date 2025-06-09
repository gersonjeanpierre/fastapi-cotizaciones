# app/schemas/customer.py
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CustomerBase(BaseModel):
    clientTypeId: int
    entityType: str
    ruc: Optional[str] = None
    dni: Optional[str] = None
    name: Optional[str] = None
    lastName: Optional[str] = None
    businessName: Optional[str] = None
    phoneNumber: Optional[str] = None
    email: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

    # Si quieres incluir las órdenes de un cliente:
    # orders: List["Order"] = []

    class Config:
        from_attributes = True

# Customer.model_rebuild()