# app/crud/customer.py
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.models import customer as models # Importa el modelo Customer
from app.schemas import customer as schemas # Importa los esquemas de Customer

# GET all customers
def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()

# GET customer by ID
def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

# CREATE customer
def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# UPDATE customer
def update_customer(db: Session, customer_id: int, customer_update: schemas.CustomerCreate):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not db_customer:
        return None # O lanzar una excepción aquí, pero el router se encarga del 404

    for key, value in customer_update.model_dump(exclude_unset=True).items():
        setattr(db_customer, key, value)

    # Aunque SQLAlchemy con onupdate=func.now() debería manejar esto, una actualización explícita es segura
    # db_customer.updated_at = datetime.now() 

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# DELETE customer
def delete_customer(db: Session, customer_id: int):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not db_customer:
        return None # O lanzar una excepción aquí

    db.delete(db_customer)
    db.commit()
    return db_customer # Retorna el objeto eliminado, útil para confirmación