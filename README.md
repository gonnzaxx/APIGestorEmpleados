# API REST Gestor de Empleados
> API de Gestión de Empleados y Departamentos es una API REST desarrollada con FastAPI que permite gestionar la información de empleados y departamentos de una organización de manera eficiente y escalable.

![Python]([https://img.shields.io/badge/Docker-Ready-blue?style=flat-square&logo=docker](https://img.shields.io/badge/python-purple?style=flat-square&logo=python))
![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=flat-square&logo=docker)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supported-blue?style=flat-square&logo=postgresql)
![SQLite](https://img.shields.io/badge/SQLite-Supported-lightgrey?style=flat-square&logo=sqlite)

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

### Características
- CRUD Completo: Operaciones de Crear, Leer, Actualizar y Eliminar para empleados y departamentos
- Relaciones de Datos: Gestión de relaciones uno-a-muchos entre departamentos y empleados
- Base de Datos Flexible: Soporte para SQLite (desarrollo) y PostgreSQL (producción)
- Dockerizado: Fácil despliegue mediante contenedores Docker
- Documentación Automática: Interfaz Swagger UI interactiva incluida
- Arquitectura Limpia: Separación de capas (modelos, schemas, servicios, routers)
- CRUD básico de empleados y departamentos

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
