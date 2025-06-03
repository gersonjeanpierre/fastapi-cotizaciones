# main.py (en la raíz del proyecto)
from fastapi import FastAPI
from app.api import api_router # Importa el api_router de tu nueva estructura
from app.core.database import Base, engine # Para la creación de tablas (si no usas migraciones)
from app.models import * # Importa todos los modelos para que Base.metadata.create_all() los detecte

app = FastAPI(
    title="Quotation API", # Título para la documentación de Swagger UI
    description="API RESTful para el sistema de cotizaciones",
    version="1.0.0",
    docs_url="/docs", # URL para Swagger UI
    redoc_url="/redoc", # URL para ReDoc
)

# Esto creará las tablas en la base de datos si aún no existen
# Esto es útil para el desarrollo inicial, pero en producción usarías un sistema de migraciones (ej. Alembic)
# Ya lo hicimos con Laravel, así que en teoría no necesitas esto.
# Sin embargo, si quieres que FastAPI maneje la creación de tablas en el futuro, puedes descomentarlo.
Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api/v1") # Incluye el router principal de tu API versionada