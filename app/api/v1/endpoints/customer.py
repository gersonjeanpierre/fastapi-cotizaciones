# app/api/v1/endpoints/customer.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas import customer as schemas
from app.crud import customer as crud # Importa las funciones CRUD
from app.core.database import get_db # Importa la dependencia de la DB

router = APIRouter(
    prefix="/customers", # Prefijo para todas las rutas en este router
    tags=["Customers"], # Etiqueta para la documentación de Swagger UI
    responses={404: {"description": "Not found"}},
)

# Crear Cliente
@router.post("/", response_model=schemas.Customer, status_code=status.HTTP_201_CREATED)
def create_customer_endpoint(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db=db, customer=customer)

# Leer Todos los Clientes
@router.get("/", response_model=List[schemas.Customer])
def read_customers_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = crud.get_customers(db=db, skip=skip, limit=limit)
    return customers

# Leer Cliente por ID
@router.get("/{customer_id}", response_model=schemas.Customer)
def read_customer_endpoint(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db=db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

# Actualizar Cliente
@router.put("/{customer_id}", response_model=schemas.Customer)
def update_customer_endpoint(customer_id: int, customer_update: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud.update_customer(db=db, customer_id=customer_id, customer_update=customer_update)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

# Eliminar Cliente
@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer_endpoint(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.delete_customer(db=db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return # Devuelve 204 sin contenido