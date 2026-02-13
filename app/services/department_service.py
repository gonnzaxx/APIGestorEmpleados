from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.db.session import get_session
from app.models.department import Department
from app.schemas.department import DepartmentCreate, DepartmentResponse, DepartmentUpdate


class DepartmentService:
    def __init__(self, session : Session = Depends(get_session)):
        self.session = session

    def create(self, department_data: DepartmentCreate) -> DepartmentResponse:
        department = Department(**department_data.model_dump())
        self.session.add(department)
        self.session.commit()
        self.session.refresh(department)
        return DepartmentResponse(**department.model_dump())


    def get_all(self):
        return self.session.exec(select(Department)).all()

    def get_by_id(self, id: int):
        return self.session.get(Department, id)


    def update(self, id: int, department_data: DepartmentUpdate) -> Department:
        department = self.session.get(Department, id)
        if not department:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")

        department_dict = department_data.model_dump(exclude_unset=True)
        for key, value in department_dict.items():
            setattr(department, key, value)

        self.session.add(department)
        self.session.commit()
        self.session.refresh(department)
        return department

    def delete(self, id: int):
        department = self.session.get(Department, id)
        if not department:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")
        self.session.delete(department)
        self.session.commit()
        return {"message": "Departamento eliminado exitosamente"}