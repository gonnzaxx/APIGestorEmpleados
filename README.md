# API REST Gestor de Empleados
> API REST que gestiona Empleados y Departamentos con base de datos SQLite o PostgreSQL.

![Python](https://img.shields.io/badge/.NET-MAUI-purple?style=flat-square&logo=dotnet)

## Instalación
### Clonar repositorio
```
git clone https://github.com/gonnzaxx/APIGestorEmpleados.git
```

### Construir la imagen de Docker
En el directorio raíz de tu proyecto (donde se encuentra el archivo Dockerfile), ejecuta el siguiente comando para construir la imagen Docker:

```
docker build -t empleados_api .
```

### Ejecutar el contendor Docker
Utilizando SQLite: 
```
docker run -d -p 8000:8000 --name APIempleadosSQLite empleados_api
```

Utilizando PostgreSQL:
  En el caso de no tener PostgreSQL instalado, utilizar estos comandos para ejecutar el contenedor:

```
docker network create empleados-network
```
```
docker run -d --name APIempleados_postgres --network empleados-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=123456 -e POSTGRES_DB=empleados_db -p 5432:5432 postgres:15-alpine
```

```
docker run -d --name APIempleados --network empleados-network -p 8000:8000 -e DATABASE_URL="postgresql://postgres:123456@APIempleados_postgres:5432/empleados_db" empleados_api
```

### Tecnologías y librerías
- Python 3.12
- FastAPI
- SQLModel
- Uvicorn
- Pydantic Settings

- SQLite
- PostgreSQL 15
- psycopg2-binary

- Docker

- API REST
- IoC
- ORM
- Patrón Repository/Service

- Swagger/OpenAPI
- Git/Github
## Estructura del Proyecto

```
APIGestorEmpleados/
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .venv
├── README.md
└── app/
    ├── main.py
    ├── core/
    │   └── config.py
    ├── db/
    │   └── session.py
    ├── models/
    │   ├── employee.py
    │   └── department.py
    ├── schemas/
    │   ├── employee.py
    │   └── department.py
    ├── services/
    │   ├── employee_service.py
    │   └── department_service.py
    └── routers/
        ├── employees.py
        └── departments.py
```

---
## Historial de versiones

### 1.0.0
- Versión inicial funcional  
- CRUD completo de empleados  
- CRUD completo de departamentos  
- Soporte SQLite y PostgreSQL  

---
## Autor

**Gonzalo Santiago Ariza**  
Proyecto académico – Desarrollo de Aplicaciones Multiplataforma  

## Licencia
Licencia MIT.
