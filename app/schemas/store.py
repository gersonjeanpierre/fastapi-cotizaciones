# app/schemas/store.py
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class StoreBase(BaseModel):
    name: str = Field(..., max_length=100)
    code: Optional[str] = Field(..., max_length=10)
    address: Optional[str] = Field(..., max_length=255)
    phone_number: Optional[str] = Field(None, max_length=15)
    email: Optional[EmailStr] = Field(None)

class StoreCreate(StoreBase):
    pass

class StoreUpdate(BaseModel):
    name: Optional[str] = Field(..., max_length=100)
    code: Optional[str] = Field(..., max_length=10)
    address: Optional[str] = Field(..., max_length=255)
    phone_number: Optional[str] = Field(None, max_length=15)
    email: Optional[EmailStr] = Field(None)

class StoreInDB(StoreBase):
    id: int
    create_at: datetime
    update_at: datetime
    delete_at: Optional[datetime] = None

    model_config = {
        "from_attributes": True
    }