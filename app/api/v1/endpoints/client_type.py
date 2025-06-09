from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas import client_type as schemas
from app.crud import client_type as crud  # Importa las funciones CRUD
from app.core.database import get_db  # Importa la dependencia de la DB

router = APIRouter(
    prefix="/client_types",
    tags=["Clients Types"], # Grupo para la documentación Swagger
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.ClientType, status_code=status.HTTP_201_CREATED)
def create_client_type(client_type: schemas.ClientTypeCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo tipo de cliente.
    """
    # Puedes añadir lógica de negocio aquí, por ejemplo, verificar si ya existe
    # db_client_type = crud.get_client_type_by_description(db, description=client_type.descripcion)
    # if db_client_type:
    #     raise HTTPException(status_code=400, detail="Client Type already registered")
    
    return crud.create_client_type(db=db, client_type=client_type)

@router.get("/", response_model=List[schemas.ClientType])
def read_all_client_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obtiene una lista de todos los tipos de cliente.
    """
    client_types = crud.get_all_client_types(db, skip=skip, limit=limit)
    return client_types

@router.get("/{client_type_id}", response_model=schemas.ClientType)
def read_client_type(client_type_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un tipo de cliente por su ID.
    """
    db_client_type = crud.get_client_type(db, client_type_id=client_type_id)
    if db_client_type is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client Type not found")
    return db_client_type

@router.put("/{client_type_id}", response_model=schemas.ClientType)
def update_client_type(client_type_id: int, client_type: schemas.ClientTypeCreate, db: Session = Depends(get_db)):
    """
    Actualiza un tipo de cliente existente por su ID.
    """
    db_client_type = crud.update_client_type(db, client_type_id=client_type_id, client_type_data=client_type)
    if db_client_type is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client Type not found")
    return db_client_type

@router.delete("/{client_type_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client_type(client_type_id: int, db: Session = Depends(get_db)):
    """
    Elimina un tipo de cliente por su ID.
    """
    db_client_type = crud.delete_client_type(db, client_type_id=client_type_id)
    if db_client_type is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client Type not found")
    return {"message": "Client Type deleted successfully"} # No devuelve contenido para 204