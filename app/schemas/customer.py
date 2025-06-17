# app/schemas/customer.py
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime
from .type_client import TypeClientInDB # Importar el schema del tipo de cliente

class CustomerBase(BaseModel):
    type_client_id: int = Field(...)
    entity_type: str = Field( ..., min_length=1, max_length=1 )
    phone_number: Optional[str] = Field( None, max_length=15 )
    email: Optional[EmailStr] = Field(None)

class CustomerCreate(CustomerBase):
    ruc: Optional[str] = Field(None, max_length=11 )
    dni: Optional[str] = Field(None, max_length=8 )
    name: Optional[str] = Field(None, max_length=35 )
    last_name: Optional[str] = Field(None, max_length=40 )
    business_name: Optional[str] = Field(None, max_length=150 )

class CustomerUpdate(BaseModel):
    type_client_id: Optional[int] = Field( ... )
    entity_type: Optional[str] = Field(..., min_length=1, max_length=1)
    ruc: Optional[str] = Field(None, max_length=11)
    dni: Optional[str] = Field(None, max_length=8)
    name: Optional[str] = Field(None, max_length=35)
    last_name: Optional[str] = Field(None, max_length=40)
    business_name: Optional[str] = Field(None, max_length=150)
    phone_number: Optional[str] = Field(None, max_length=15)
    email: Optional[EmailStr] = Field(None)

class CustomerInDB(CustomerBase):
    id: int
    ruc: Optional[str] = None
    dni: Optional[str] = None
    name: Optional[str] = None
    last_name: Optional[str] = None
    business_name: Optional[str] = None
    create_at: datetime
    update_at: datetime
    delete_at: Optional[datetime] = None

    # Opcional: Incluir el tipo de cliente anidado para respuestas más ricas
    type_client: TypeClientInDB

    model_config = {
        "from_attributes": True
    }