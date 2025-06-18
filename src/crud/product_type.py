from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from src.models import product_type as models  # Importa el modelo ProductType
from src.schemas import product_type as schemas  # Importa los esquemas de ProductType

# GET all product types
def get_product_types(db: Session, skip: int = 0, limit: int = 100) -> List[models.ProductType]:
    return db.query(models.ProductType).offset(skip).limit(limit).all()

# GET product type by ID
def get_product_type(db: Session, product_type_id: int) -> Optional[models.ProductType]:
    return db.query(models.ProductType).filter(models.ProductType.id == product_type_id).first()

# CREATE product type
def create_product_type(db: Session, product_type: schemas.ProductTypeCreate) -> models.ProductType:
    db_product_type = models.ProductType(**product_type.model_dump())
    db.add(db_product_type)
    db.commit()
    db.refresh(db_product_type)
    return db_product_type

# UPDATE product type
def update_product_type(db: Session, product_type_id: int, product_type_update: schemas.ProductTypeCreate) -> Optional[models.ProductType]:
    db_product_type = db.query(models.ProductType).filter(models.ProductType.id == product_type_id).first()
    if not db_product_type:
        return None  # O lanzar una excepción aquí, pero el router se encarga del 404
    for key, value in product_type_update.model_dump(exclude_unset=True).items():
        setattr(db_product_type, key, value)
    db.add(db_product_type)
    db.commit()
    db.refresh(db_product_type)
    return db_product_type

# DELETE product type
def delete_product_type(db: Session, product_type_id: int) -> Optional[models.ProductType]:
    db_product_type = db.query(models.ProductType).filter(models.ProductType.id == product_type_id).first()
    if not db_product_type:
        return None
    db.delete(db_product_type)
    db.commit()
    return db_product_type