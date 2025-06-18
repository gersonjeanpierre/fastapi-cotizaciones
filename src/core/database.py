from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL de conexión a tu base de datos PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg://postgres:L4z4r0$@127.0.0.1:5432/Cotizacion"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)  # echo=True para ver las consultas SQL en la consola
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Función para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()