# APIGestorEmpleados
## API de FastAPI con SQLModel
API que gestiona Empleados y Departamentos con una base de datos SQLite o PostgreSQL.

### Construir la imagen de Docker
En el directorio raíz de tu proyecto (donde se encuentra el archivo Dockerfile), ejecuta el siguiente comando para construir la imagen Docker:

```
docker build -t empleados_api .
```

### Ejecutar el contendor Docker
Utilizando SQLite: 
```
docker run -d -p 8000:8000 empleados_api
```

Utilizando PostgreeSQL:
```
docker run -d -p 8000:8000 -e DATABASE_URL="postgresql://usuario:password@host:5432/nombre_bd" -e DEBUG="False" empleados_api
```

