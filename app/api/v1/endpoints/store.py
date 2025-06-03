from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas import store as schemas
from app.crud import store as crud
from app.core.database import get_db

router = APIRouter(
    prefix="/stores", # Prefijo para todas las rutas en este router
    tags=["Stores"], # Etiqueta para la documentación de Swagger UI
    responses={404: {"description": "Not found"}},
)

# Crear Tienda
@router.post("/", response_model=schemas.Store, status_code=status.HTTP_201_CREATED)
def create_store_endpoint(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    return crud.create_store(db=db, store=store)

# Leer Todas las Tiendas
@router.get("/", response_model=List[schemas.Store])
def read_stores_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stores = crud.get_stores(db=db, skip=skip, limit=limit)
    return stores

# Leer Tienda por ID
@router.get("/{store_id}", response_model=schemas.Store)
def read_store_endpoint(store_id: int, db: Session = Depends(get_db)):
    db_store = crud.get_store(db=db, store_id=store_id)
    if db_store is None:
        raise HTTPException(status_code=404, detail="Store not found")
    return db_store

# Actualizar Tienda
@router.put("/{store_id}", response_model=schemas.Store)
def update_store_endpoint(store_id: int, store_update: schemas.StoreCreate, db: Session = Depends(get_db)):
    db_store = crud.update_store(db=db, store_id=store_id, store_update=store_update)
    if db_store is None:
        raise HTTPException(status_code=404, detail="Store not found")
    return db_store

# Eliminar Tienda
@router.delete("/{store_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_store_endpoint(store_id: int, db: Session = Depends(get_db)):
    db_store = crud.delete_store(db=db, store_id=store_id)
    if db_store is None:
        raise HTTPException(status_code=404, detail="Store not found")
    return # Devuelve 204 sin contenido