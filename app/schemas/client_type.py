# app/schemas/client_type.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class ClientTypeBase(BaseModel):
    typeName: str
    profitMargin: Decimal

class ClientTypeCreate(ClientTypeBase):
    pass

class ClientType(ClientTypeBase):
    id: int
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

    class Config:
        from_attributes = True