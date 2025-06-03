from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.models import product_extra_option as models # Importa el modelo ProductExtraOption
from app.schemas import product_extra_option as schemas # Importa los esquemas de ProductExtraOption

# GET all product extra options
def get_product_extra_options(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProductExtraOption).offset(skip).limit(limit).all()

# GET product extra option by ID
def get_product_extra_option(db: Session, product_extra_option_id: int):
    return db.query(models.ProductExtraOption).filter(models.ProductExtraOption.id == product_extra_option_id).first()

# CREATE product extra option
def create_product_extra_option(db: Session, option: schemas.ProductExtraOptionCreate):
    db_option = models.ProductExtraOption(**option.model_dump())
    db.add(db_option)
    db.commit()
    db.refresh(db_option)
    return db_option

# UPDATE product extra option
def update_product_extra_option(db: Session, product_extra_option_id: int, option_update: schemas.ProductExtraOptionCreate):
    db_option = db.query(models.ProductExtraOption).filter(models.ProductExtraOption.id == product_extra_option_id).first()
    if not db_option:
        return None

    for key, value in option_update.model_dump(exclude_unset=True).items():
        setattr(db_option, key, value)
    
    # SQLAlchemy gestiona updated_at automáticamente via onupdate=func.now()
    db.add(db_option)
    db.commit()
    db.refresh(db_option)
    return db_option

# DELETE product extra option
def delete_product_extra_option(db: Session, product_extra_option_id: int):
    db_option = db.query(models.ProductExtraOption).filter(models.ProductExtraOption.id == product_extra_option_id).first()
    if not db_option:
        return None

    db.delete(db_option)
    db.commit()
    return db_option # Retorna el objeto eliminado