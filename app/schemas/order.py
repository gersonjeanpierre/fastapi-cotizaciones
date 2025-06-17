# app/schemas/order.py
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# Importar schemas anidados (se resuelven al runtime)
from .customer import CustomerInDB
from .store import StoreInDB
from .order_status import OrderStatusInDB

class OrderDetailCreate(BaseModel):
    product_id: int = Field(...)
    quantity: int = Field(..., gt=0)
    # unit_price y total_extra_options se calculan en el backend si es posible,
    # o se envían desde el frontend si el frontend es la fuente de verdad para esos cálculos.
    # Para esta API, asumimos que el frontend envía los precios calculados para el detalle.
    unit_price: float = Field(..., gt=0)
    total_extra_options: float = Field(0.00, ge=0)
    # subtotal se calculará en el backend: quantity * (unit_price + total_extra_options)
    extra_option_ids: Optional[List[int]] = None # IDs de las opciones extra para este detalle de producto

class OrderDetailInDB(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    unit_price: float
    total_extra_options: float
    subtotal: float
    create_at: datetime
    delete_at: Optional[datetime] = None
    # product: ProductInDB # Opcional: anidar el producto completo
    # extra_options_details: List[OrderDetailExtraOptionInDB] # Opcional: anidar detalles de opciones

    model_config = {"from_attributes": True}

class OrderCreate(BaseModel):
    customer_id: int = Field(...)
    store_id: int = Field(...)
    order_status_id: int = Field(...) # Ej. 1 para 'Pendiente'
    payment_method: Optional[str] = Field(None, max_length=50)
    shipping_address: Optional[str] = Field(None, max_length=200)
    notes: Optional[str] = Field(None, max_length=200)
    
    details: List[OrderDetailCreate] # Lista de detalles del pedido

class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    store_id: Optional[int] = None
    order_status_id: Optional[int] = None
    payment_method: Optional[str] = None
    shipping_address: Optional[str] = None
    notes: Optional[str] = None
    # total_amount, profit_margin, discount_applied, final_amount se calcularán en el backend

class OrderInDB(BaseModel):
    id: int
    customer_id: int
    store_id: int
    order_status_id: int
    order_date: datetime
    total_amount: float
    profit_margin: float
    discount_applied: float
    final_amount: float
    payment_method: Optional[str] = None
    shipping_address: Optional[str] = None
    notes: Optional[str] = None
    create_at: datetime
    update_at: datetime
    delete_at: Optional[datetime] = None

    customer: CustomerInDB # Anidar cliente
    store: StoreInDB # Anidar tienda
    status: OrderStatusInDB # Anidar estado
    details: List[OrderDetailInDB] # Anidar detalles del pedido

    model_config = {"from_attributes": True}

class OrderDetailExtraOptionBase(BaseModel):
    order_detail_id: int
    extra_option_id: int
    price_at_order: float # Precio de la extra en el momento del pedido

class OrderDetailExtraOptionInDB(OrderDetailExtraOptionBase):
    model_config = {"from_attributes": True}