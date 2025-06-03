from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.models import store as models # Importa el modelo Store
from app.schemas import store as schemas # Importa los esquemas de Store

# GET all stores
def get_stores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Store).offset(skip).limit(limit).all()

# GET store by ID
def get_store(db: Session, store_id: int):
    return db.query(models.Store).filter(models.Store.id == store_id).first()

# CREATE store
def create_store(db: Session, store: schemas.StoreCreate):
    db_store = models.Store(**store.model_dump())
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

# UPDATE store
def update_store(db: Session, store_id: int, store_update: schemas.StoreCreate):
    db_store = db.query(models.Store).filter(models.Store.id == store_id).first()
    if not db_store:
        return None

    for key, value in store_update.model_dump(exclude_unset=True).items():
        setattr(db_store, key, value)
    
    # SQLAlchemy gestiona updated_at automáticamente via onupdate=func.now()
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

# DELETE store
def delete_store(db: Session, store_id: int):
    db_store = db.query(models.Store).filter(models.Store.id == store_id).first()
    if not db_store:
        return None

    db.delete(db_store)
    db.commit()
    return db_store # Retorna el objeto eliminado