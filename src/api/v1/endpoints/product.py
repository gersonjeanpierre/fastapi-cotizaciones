from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.schemas import product_type as schemas
from src.crud import product as crud
from src.core.database import get_db

router = APIRouter(
    prefix="/products", # Prefijo para todas las rutas en este router
    tags=["Products"], # Etiqueta para la documentación de Swagger UI
    responses={404: {"description": "Not found"}},
)

# Crear Producto
@router.post("/", response_model=schemas.Product, status_code=status.HTTP_201_CREATED)
def create_product_endpoint(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

# Leer Todos los Productos
@router.get("/", response_model=List[schemas.Product])
def read_products_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db=db, skip=skip, limit=limit)
    return products

# Leer Producto por ID
@router.get("/{product_id}", response_model=schemas.Product)
def read_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# Actualizar Producto
@router.put("/{product_id}", response_model=schemas.Product)
def update_product_endpoint(product_id: int, product_update: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.update_product(db=db, product_id=product_id, product_update=product_update)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# Eliminar Producto
@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return # Devuelve 204 sin contenido