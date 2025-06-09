from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class OrderStatusBase(BaseModel):
    name: str # varchar(50)
    description: Optional[str] = None # text

class OrderStatusCreate(OrderStatusBase):
    pass # No hay campos adicionales requeridos para la creación

class OrderStatus(OrderStatusBase):
    id: int
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

    # Si quieres cargar las órdenes relacionadas con este estado, descomenta:
    # from .order import Order # Importación relativa
    # orders: List[Order] = []

    class Config:
        from_attributes = True # Permite que el modelo Pydantic lea datos de un objeto ORM

# OrderStatus.model_rebuild() # Descomentar si hay referencias circulares en este archivo o con otros