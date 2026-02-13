from fastapi import FastAPI
from sqlmodel import SQLModel
from app.db.session import engine

from app.routers import employees, departments

app = FastAPI()


# Registrar las rutas
app.include_router(departments.router)
app.include_router(employees.router)


# Crear tablas en la base de datos si no existen
def init_db():
    SQLModel.metadata.create_all(engine)

init_db()