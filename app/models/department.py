
from sqlmodel import SQLModel, Field, Relationship

class Department(SQLModel, table = True):
    id: int | None = Field(default = None, primary_key = True)
    name : str | None = None
    image_uri : str | None = None

    employees : list["Employee"] = Relationship(back_populates="department", cascade_delete=True)
