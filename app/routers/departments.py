from fastapi import APIRouter, Depends

from app.schemas.department import DepartmentResponse, DepartmentCreate, DepartmentUpdate
from app.services.department_service import DepartmentService

router = APIRouter(prefix="/departments", tags=["Departments"])

@router.post("/", response_model=DepartmentResponse)
async def create_department(department: DepartmentCreate, service: DepartmentService = Depends()):
    return service.create(department)


@router.get("/", response_model=list[DepartmentResponse])
async def read_departments(service: DepartmentService = Depends()):
    return service.get_all()

@router.get("/{id}", response_model=DepartmentResponse)
async def read_department(id: int, service: DepartmentService = Depends()):
    return service.get_by_id(id)


@router.patch("/{id}", response_model=DepartmentResponse)
async def update_department(id: int, department_data: DepartmentUpdate, service: DepartmentService = Depends()):
    return service.update(id, department_data)

@router.delete("/{id}", response_model=dict)
async def delete_department(id: int, service: DepartmentService = Depends()):
    return service.delete(id)