from fastapi import APIRouter, Depends, Query

from app.schemas.employee import EmployeeResponse, EmployeeCreate, EmployeeUpdate
from app.services.employee_service import EmployeeService

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/", response_model = EmployeeResponse)
async def create_employee(employee: EmployeeCreate, service: EmployeeService = Depends()):
    return service.create(employee)


@router.get("/", response_model = list[EmployeeResponse])
async def read_employees(service: EmployeeService = Depends()):
    return service.get_all()

@router.get("/{id}", response_model = EmployeeResponse)
async def read_employee(id: int, service: EmployeeService = Depends()):
    return service.get_by_id(id)

@router.patch("/{id}", response_model = EmployeeResponse)
async def update_employee(id: int, employee_data: EmployeeUpdate, service: EmployeeService = Depends()):
    return service.update(id, employee_data)

@router.delete("/{id}", response_model = dict)
async def delete_employee(id: int, service: EmployeeService = Depends()):
    return service.delete(id)