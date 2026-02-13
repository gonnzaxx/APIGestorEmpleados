from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class Employee(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    last_name : str
    address : str
    phone : int
    image_uri : str
    department_id : int =  Field(foreign_key = "department.id")

    department : Optional["Department"] = Relationship(back_populates="employees")