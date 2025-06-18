from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from src.schemas import product_type as schemas
from src.crud import product_type as crud
from src.core.database import get_db

router = APIRouter(
    prefix="/product-types",
    tags=["Product Types"],
    responses={404: {"description": "Not found"}},
)

# Create Product Type
@router.post("/", response_model=schemas.ProductTypeInDB, status_code=status.HTTP_201_CREATED)
def create_product_type_endpoint(product_type: schemas.ProductTypeCreate, db: Session = Depends(get_db)):
    return crud.create_product_type(db=db, product_type=product_type)

# Read All Product Types
@router.get("/", response_model=List[schemas.ProductTypeInDB])
def read_product_types_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    product_types = crud.get_product_types(db=db, skip=skip, limit=limit)
    return product_types

# Read Product Type by ID
@router.get("/{product_type_id}", response_model=schemas.ProductTypeInDB)
def read_product_type_endpoint(product_type_id: int, db: Session = Depends(get_db)):
    db_product_type = crud.get_product_type(db=db, product_type_id=product_type_id)
    if db_product_type is None:
        raise HTTPException(status_code=404, detail="Product Type not found")
    return db_product_type

# Update Product Type
@router.put("/{product_type_id}", response_model=schemas.ProductTypeInDB)
def update_product_type_endpoint(product_type_id: int, product_type_update: schemas.ProductTypeCreate, db: Session = Depends(get_db)):
    db_product_type = crud.update_product_type(db=db, product_type_id=product_type_id, product_type_update=product_type_update)
    if db_product_type is None:
        raise HTTPException(status_code=404, detail="Product Type not found")  
    return db_product_type

# Delete Product Type
@router.delete("/{product_type_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product_type_endpoint(product_type_id: int, db: Session = Depends(get_db)):
    db_product_type = crud.delete_product_type(db=db, product_type_id=product_type_id)
    if db_product_type is None:
        raise HTTPException(status_code=404, detail="Product Type not found")
    return  # Returns 204 No Content