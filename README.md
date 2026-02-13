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

En el caso de no tener PostgreSQL instalado, utilizar estos comandos para ejecutar un contenedor:

```
docker network create empleados-network
```
```
docker run -d --name APIempleados_postgres --network empleados-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=123456 -e POSTGRES_DB=empleados_db -p 5432:5432 postgres:15-alpine
```

```
docker run -d --name APIempleados --network empleados-network -p 8000:8000 -e DATABASE_URL="postgresql://postgres:123456@APIempleados_postgres:5432/empleados_db" empleados_api
```


