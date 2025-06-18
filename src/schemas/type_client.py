# app/schemas/type_client.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TypeClientBase(BaseModel):
    code: str = Field(..., max_length=6)
    name: str = Field(..., max_length=50)
    margin: float = Field(..., ge= 0 , le= 1 ) 
    description: Optional[str] = Field(None)

class TypeClientCreate(TypeClientBase):
    pass

class TypeClientUpdate(BaseModel):
    code: Optional[str] = Field(..., max_length=6 ) 
    name: Optional[str] = Field(..., max_length=50 )
    margin: Optional[float] = Field(..., ge= 0 , le= 1 ) 
    description: Optional[str] = Field(None)

class TypeClientInDB(TypeClientBase):
    id: int
    create_at: datetime
    update_at: datetime
    delete_at: Optional[datetime] = None

    model_config = {
        "from_attributes": True # Pydantic v2
    }