# Challenge DataBiz - ToDo API

API RESTful para gestión de tareas construida con FastAPI y PostgreSQL.

## 📋 Descripción

Esta aplicación proporciona una API completa para gestionar tareas (ToDo) con operaciones CRUD básicas. Desarrollada como parte del challenge técnico para DataBiz.

## 🚀 Tecnologías

- **FastAPI** - Framework web moderno y rápido para Python
- **PostgreSQL** - Base de datos relacional
- **SQLAlchemy** - ORM para Python
- **Docker & Docker Compose** - Containerización y orquestación
- **Pydantic** - Validación de datos

## 📁 Estructura del Proyecto

```
challenge-databiz/
├── app/
│   ├── main.py          # Punto de entrada de la API y endpoints
│   ├── models.py        # Modelos SQLAlchemy
│   ├── schemas.py       # Esquemas Pydantic
│   ├── crud.py          # Operaciones de base de datos
│   └── database.py      # Configuración de la base de datos
├── docker-compose.yml   # Orquestación de contenedores
├── Dockerfile           # Imagen de la aplicación
├── requirements.txt     # Dependencias de Python
└── README.md
```

## 🔧 Requisitos Previos

- Docker
- Docker Compose

## ⚙️ Configuración

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/challenge-databiz.git
cd challenge-databiz
```

2. Crear archivo `.env` en la raíz del proyecto:
```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=tododb
DATABASE_URL=postgresql://postgres:postgres@db:5432/tododb
```

## 🐳 Ejecución con Docker

1. Construir y levantar los contenedores:
```bash
docker-compose up --build
```

2. La API estará disponible en: `http://localhost:8000`

3. Documentación interactiva (Swagger UI): `http://localhost:8000/docs`

4. Documentación alternativa (ReDoc): `http://localhost:8000/redoc`

## 📡 Endpoints de la API

### Health Check
- `GET /health` - Verifica que la API está funcionando

### Tareas (Tasks)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/tasks` | Crear una nueva tarea |
| GET | `/tasks` | Listar todas las tareas |
| GET | `/tasks/{task_id}` | Obtener una tarea específica |
| PUT | `/tasks/{task_id}` | Actualizar una tarea |
| DELETE | `/tasks/{task_id}` | Eliminar una tarea |

### Ejemplos de Uso

#### Crear una tarea
```bash
curl -X POST "http://localhost:8000/tasks" \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Completar el challenge",
    "descripcion": "Implementar API con FastAPI",
    "completada": false
  }'
```

#### Listar todas las tareas
```bash
curl -X GET "http://localhost:8000/tasks"
```

#### Obtener una tarea específica
```bash
curl -X GET "http://localhost:8000/tasks/1"
```

#### Actualizar una tarea
```bash
curl -X PUT "http://localhost:8000/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Challenge completado",
    "completada": true
  }'
```

#### Eliminar una tarea
```bash
curl -X DELETE "http://localhost:8000/tasks/1"
```

## 🗃️ Modelo de Datos

### Task (Tarea)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | Integer | Identificador único (auto-generado) |
| titulo | String(200) | Título de la tarea (requerido) |
| descripcion | Text | Descripción detallada (opcional) |
| completada | Boolean | Estado de completitud (default: false) |
| fecha_creacion | DateTime | Fecha y hora de creación (auto-generado) |

## 🛠️ Desarrollo Local (sin Docker)

1. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar PostgreSQL local y crear archivo `.env`

4. Ejecutar la aplicación:
```bash
uvicorn app.main:app --reload
```

## 🧪 Testing

Para probar la API, puedes usar:
- La interfaz Swagger UI en `/docs`
- Herramientas como Postman, Insomnia o cURL
- Scripts de prueba automatizados (pytest - por implementar)

## 🔍 Notas Técnicas

- La aplicación crea las tablas automáticamente al iniciar
- Utiliza SQLAlchemy ORM con tipado moderno (Mapped)
- Validación de datos con Pydantic v2
- Soporte para PostgreSQL con timezone-aware datetimes
- Contenedores con restart policy para mayor resiliencia

## 📝 Licencia

Este proyecto fue desarrollado como parte de un challenge técnico para DataBiz.

## 👤 Autor

**CR7**

---

**Challenge DataBiz - 2026**

