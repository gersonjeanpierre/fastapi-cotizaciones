from sqlalchemy.orm import Session
from app.models import client_type as models
from app.schemas import client_type as schemas

# Obtener todos los tipos de cliente
def get_all_client_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ClientType).offset(skip).limit(limit).all()

# Obtener un tipo de cliente por ID
def get_client_type(db: Session, client_type_id: int):
    return db.query(models.ClientType).filter(models.ClientType.id == client_type_id).first()


# Crear un nuevo tipo de cliente
def create_client_type(db: Session, client_type: schemas.ClientTypeCreate):
    db_client_type = models.ClientType(**client_type.model_dump())
    db.add(db_client_type)
    db.commit()
    db.refresh(db_client_type)
    return db_client_type

# Actualizar un tipo de cliente existente
def update_client_type(db: Session, client_type_id: int, client_type_data: schemas.ClientTypeCreate):
    db_client_type = db.query(models.ClientType).filter(models.ClientType.id == client_type_id).first()
    if db_client_type:
        # Actualiza solo los campos que no son None en client_type_data
        for field, value in client_type_data.model_dump(exclude_unset=True).items(): # model_dump para Pydantic v2
            setattr(db_client_type, field, value)
        db.add(db_client_type) # Re-add para asegurar que SQLAlchemy detecte los cambios
        db.commit()
        db.refresh(db_client_type)
    return db_client_type

# Eliminar un tipo de cliente
def delete_client_type(db: Session, client_type_id: int):
    db_client_type = db.query(models.ClientType).filter(models.ClientType.id == client_type_id).first()
    if db_client_type:
        db.delete(db_client_type)
        db.commit()
    return db_client_type # Devuelve el objeto eliminado o None si no se encontró