from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.db.session import get_session
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeResponse, EmployeeUpdate

class EmployeeService:
    def __init__(self, session : Session = Depends(get_session)):
        self.session = session


    def create(self, employee_data: EmployeeCreate) -> EmployeeResponse:
        employee = Employee(**employee_data.model_dump())
        self.session.add(employee)
        self.session.commit()
        self.session.refresh(employee)

        if employee.department_id:
            employee.department
        return employee


    def get_all(self):
        return self.session.exec(select(Employee)).all()

    def get_by_id(self, id: int):
        employee = self.session.get(Employee, id)
        if employee and employee.department_id:
            employee.department
        return employee


    def update(self, id: int, employee_data: EmployeeUpdate) -> Employee:
        employee = self.session.get(Employee, id)
        if not employee:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")

        employee_dict = employee_data.model_dump(exclude_unset=True)
        for key, value in employee_dict.items():
            setattr(employee, key, value)

        self.session.add(employee)
        self.session.commit()
        self.session.refresh(employee)

        if employee.department_id:
            employee.department
        return employee

    def delete(self, id: int):
        employee = self.session.get(Employee, id)
        if not employee:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")
        self.session.delete(employee)
        self.session.commit()
        return {"message": "Empleado eliminado exitosamente"}