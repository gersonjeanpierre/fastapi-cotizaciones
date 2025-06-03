# ... (otras clases BaseModel)

# Esquemas para Customer
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CustomerBase(BaseModel):
    entity_type: str # char(1)
    ruc: Optional[str] = None # char(11)
    dni: Optional[str] = None # char(8)
    name: Optional[str] = None # varchar(35)
    last_name: Optional[str] = None # varchar(40)
    business_name: Optional[str] = None # varchar(150)
    phone_number: Optional[str] = None # varchar(15)
    email: Optional[str] = None # varchar(60)

class CustomerCreate(CustomerBase):
    # No hay campos adicionales requeridos para la creación
    pass

class Customer(CustomerBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True # Permite que el modelo Pydantic lea datos de un objeto ORM


