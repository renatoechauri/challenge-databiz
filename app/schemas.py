from datetime import datetime
from pydantic import BaseModel, ConfigDict

# Schema para la creación y actualización de tareas
class TaskBase(BaseModel):
    titulo: str
    descripcion: str | None = None
    completada: bool = False

# Schema específico para la creación de tareas
class TaskCreate(TaskBase):
    pass

# Schema específico para la actualización de tareas
class TaskUpdate(BaseModel):
    titulo: str
    descripcion: str | None = None
    completada: bool | None = None

# Schema para la salida de tareas
class TaskOut(TaskBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    fecha_creacion: datetime