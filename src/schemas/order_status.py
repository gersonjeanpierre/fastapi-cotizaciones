# app/schemas/order_status.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class OrderStatusBase(BaseModel):
    code: str = Field(..., max_length=10)
    name: str = Field(..., max_length=50)
    description: Optional[str] = Field(None)

class OrderStatusCreate(OrderStatusBase):
    pass

class OrderStatusUpdate(BaseModel):
    code: Optional[str] = Field(..., max_length=10)
    name: Optional[str] = Field(..., max_length=50)
    description: Optional[str] = Field(None)

class OrderStatusInDB(OrderStatusBase):
    id: int
    create_at: datetime
    update_at: datetime
    delete_at: Optional[datetime] = None

    model_config = {
        "from_attributes": True
    }