from sqlmodel import SQLModel

from app.models.department import Department


class EmployeeCreate(SQLModel):
    name: str
    last_name: str
    address: str | None = None
    phone: int | None = None
    image_uri: str | None = None
    department_id: int

class EmployeeResponse(EmployeeCreate):
    id: int
    department : Department

class EmployeeUpdate(SQLModel):
    name: str | None = None
    last_name: str | None = None
    address: str | None = None
    phone: int | None = None
    image_uri: str | None = None
    department_id: int | None = None