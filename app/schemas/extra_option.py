# app/schemas/extra_option.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ExtraOptionBase(BaseModel):
    name: str = Field(..., max_length=255 )
    price_modifier: float = Field(... )
    description: Optional[str] = Field(None )

class ExtraOptionCreate(ExtraOptionBase):
    pass

class ExtraOptionUpdate(BaseModel):
    name: Optional[str] = Field(..., max_length=255)
    price_modifier: Optional[float] = Field(...)
    description: Optional[str] = Field(None)

class ExtraOptionInDB(ExtraOptionBase):
    id: int
    create_at: datetime
    update_at: datetime
    delete_at: Optional[datetime] = None

    model_config = {
        "from_attributes": True
    }