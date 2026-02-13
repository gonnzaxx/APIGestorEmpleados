from sqlmodel import SQLModel


class DepartmentCreate(SQLModel):
    name : str
    image_uri : str | None = None


class DepartmentResponse(DepartmentCreate):
    id: int

class DepartmentUpdate(SQLModel):
    name: str | None = None
    image_uri: str | None = None
