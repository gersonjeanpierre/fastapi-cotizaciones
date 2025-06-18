from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.schemas import product_extra_option as schemas
from src.crud import product_extra_option as crud
from src.core.database import get_db

router = APIRouter(
    prefix="/product_extra_options", # Prefijo para todas las rutas en este router
    tags=["Product Extra Options"], # Etiqueta para la documentación de Swagger UI
    responses={404: {"description": "Not found"}},
)

# Crear Opción Extra de Producto
@router.post("/", response_model=schemas.ProductExtraOption, status_code=status.HTTP_201_CREATED)
def create_product_extra_option_endpoint(option: schemas.ProductExtraOptionCreate, db: Session = Depends(get_db)):
    # Opcional: Verificar si el product_id existe antes de crear la opción extra
    # from src.crud import product as product_crud
    # db_product = product_crud.get_product(db, option.product_id)
    # if db_product is None:
    #     raise HTTPException(status_code=400, detail="Product ID does not exist")

    return crud.create_product_extra_option(db=db, option=option)

# Leer Todas las Opciones Extra de Producto
@router.get("/", response_model=List[schemas.ProductExtraOption])
def read_product_extra_options_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    options = crud.get_product_extra_options(db=db, skip=skip, limit=limit)
    return options

# Leer Opción Extra de Producto por ID
@router.get("/{product_extra_option_id}", response_model=schemas.ProductExtraOption)
def read_product_extra_option_endpoint(product_extra_option_id: int, db: Session = Depends(get_db)):
    db_option = crud.get_product_extra_option(db=db, product_extra_option_id=product_extra_option_id)
    if db_option is None:
        raise HTTPException(status_code=404, detail="Product Extra Option not found")
    return db_option

# Actualizar Opción Extra de Producto
@router.put("/{product_extra_option_id}", response_model=schemas.ProductExtraOption)
def update_product_extra_option_endpoint(product_extra_option_id: int, option_update: schemas.ProductExtraOptionCreate, db: Session = Depends(get_db)):
    db_option = crud.update_product_extra_option(db=db, product_extra_option_id=product_extra_option_id, option_update=option_update)
    if db_option is None:
        raise HTTPException(status_code=404, detail="Product Extra Option not found")
    return db_option

# Eliminar Opción Extra de Producto
@router.delete("/{product_extra_option_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product_extra_option_endpoint(product_extra_option_id: int, db: Session = Depends(get_db)):
    db_option = crud.delete_product_extra_option(db=db, product_extra_option_id=product_extra_option_id)
    if db_option is None:
        raise HTTPException(status_code=404, detail="Product Extra Option not found")
    return # Devuelve 204 sin contenido