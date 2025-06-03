# app/schemas/client_type.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class ClientTypeBase(BaseModel):
    type_name: str
    profit_margin: Decimal

class ClientTypeCreate(ClientTypeBase):
    pass

class ClientType(ClientTypeBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True