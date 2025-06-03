from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas import order_status as schemas
from app.crud import order_status as crud
from app.core.database import get_db

router = APIRouter(
    prefix="/order_statuses", # Prefijo para todas las rutas en este router
    tags=["Order Statuses"], # Etiqueta para la documentación de Swagger UI
    responses={404: {"description": "Not found"}},
)

# Crear Estado de Orden
@router.post("/", response_model=schemas.OrderStatus, status_code=status.HTTP_201_CREATED)
def create_order_status_endpoint(order_status: schemas.OrderStatusCreate, db: Session = Depends(get_db)):
    return crud.create_order_status(db=db, order_status=order_status)

# Leer Todos los Estados de Orden
@router.get("/", response_model=List[schemas.OrderStatus])
def read_order_statuses_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    order_statuses = crud.get_order_statuses(db=db, skip=skip, limit=limit)
    return order_statuses

# Leer Estado de Orden por ID
@router.get("/{order_status_id}", response_model=schemas.OrderStatus)
def read_order_status_endpoint(order_status_id: int, db: Session = Depends(get_db)):
    db_order_status = crud.get_order_status(db=db, order_status_id=order_status_id)
    if db_order_status is None:
        raise HTTPException(status_code=404, detail="Order Status not found")
    return db_order_status

# Actualizar Estado de Orden
@router.put("/{order_status_id}", response_model=schemas.OrderStatus)
def update_order_status_endpoint(order_status_id: int, order_status_update: schemas.OrderStatusCreate, db: Session = Depends(get_db)):
    db_order_status = crud.update_order_status(db=db, order_status_id=order_status_id, order_status_update=order_status_update)
    if db_order_status is None:
        raise HTTPException(status_code=404, detail="Order Status not found")
    return db_order_status

# Eliminar Estado de Orden
@router.delete("/{order_status_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order_status_endpoint(order_status_id: int, db: Session = Depends(get_db)):
    db_order_status = crud.delete_order_status(db=db, order_status_id=order_status_id)
    if db_order_status is None:
        raise HTTPException(status_code=404, detail="Order Status not found")
    return # Devuelve 204 sin contenido