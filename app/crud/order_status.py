from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.models import order_status as models # Importa el modelo OrderStatus
from app.schemas import order_status as schemas # Importa los esquemas de OrderStatus

# GET all order statuses
def get_order_statuses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.OrderStatus).offset(skip).limit(limit).all()

# GET order status by ID
def get_order_status(db: Session, order_status_id: int):
    return db.query(models.OrderStatus).filter(models.OrderStatus.id == order_status_id).first()

# CREATE order status
def create_order_status(db: Session, order_status: schemas.OrderStatusCreate):
    db_order_status = models.OrderStatus(**order_status.model_dump())
    db.add(db_order_status)
    db.commit()
    db.refresh(db_order_status)
    return db_order_status

# UPDATE order status
def update_order_status(db: Session, order_status_id: int, order_status_update: schemas.OrderStatusCreate):
    db_order_status = db.query(models.OrderStatus).filter(models.OrderStatus.id == order_status_id).first()
    if not db_order_status:
        return None

    for key, value in order_status_update.model_dump(exclude_unset=True).items():
        setattr(db_order_status, key, value)
    
    # SQLAlchemy gestiona updated_at automáticamente via onupdate=func.now()
    db.add(db_order_status)
    db.commit()
    db.refresh(db_order_status)
    return db_order_status

# DELETE order status
def delete_order_status(db: Session, order_status_id: int):
    db_order_status = db.query(models.OrderStatus).filter(models.OrderStatus.id == order_status_id).first()
    if not db_order_status:
        return None

    db.delete(db_order_status)
    db.commit()
    return db_order_status # Retorna el objeto eliminado