from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class StoreBase(BaseModel):
    code: str # char(8)
    description: str # varchar(100)

class StoreCreate(StoreBase):
    pass # No hay campos adicionales requeridos para la creación

class Store(StoreBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    # Si quieres cargar las órdenes relacionadas con la tienda, descomenta:
    # from .order import Order # Importación relativa
    # orders: List[Order] = []

    class Config:
        from_attributes = True # Permite que el modelo Pydantic lea datos de un objeto ORM

# Store.model_rebuild() # Descomentar si hay referencias circulares en este archivo o con otros