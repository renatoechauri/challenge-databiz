from datetime import datetime
from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    titulo: str
    descripcion: str | None = None
    completada: bool = False


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    titulo: str
    descripcion: str | None = None
    completada: bool | None = None


class TaskOut(TaskBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    fecha_creacion: datetime