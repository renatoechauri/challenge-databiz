from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from .database import Base, engine, get_db
from .schemas import TaskCreate, TaskUpdate, TaskOut
from . import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ToDo API")


# Exception Handlers
@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Error de base de datos",
            "message": "Ocurrió un error al procesar la solicitud en la base de datos"
        }
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Error interno del servidor",
            "message": "Ocurrió un error inesperado"
        }
    )


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tasks", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_task(db, payload)
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Error de integridad en los datos"
        )
    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Error al crear la tarea en la base de datos"
        )


@app.get("/tasks", response_model=list[TaskOut])
def list_tasks(db: Session = Depends(get_db)):
    try:
        return crud.list_tasks(db)
    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Error al obtener las tareas"
        )


@app.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    if task_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="El ID de la tarea debe ser un número positivo"
        )
    
    try:
        task = crud.get_task(db, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task no encontrada")
        return task
    except HTTPException:
        raise
    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Error al obtener la tarea"
        )


@app.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db)):
    if task_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="El ID de la tarea debe ser un número positivo"
        )
    
    try:
        task = crud.get_task(db, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task no encontrada")
        return crud.update_task(db, task, payload)
    except HTTPException:
        raise
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Error de integridad en los datos"
        )
    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Error al actualizar la tarea"
        )


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    if task_id <= 0:
        raise HTTPException(
            status_code=400,
            detail="El ID de la tarea debe ser un número positivo"
        )
    
    try:
        task = crud.get_task(db, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task no encontrada")
        crud.delete_task(db, task)
        return None
    except HTTPException:
        raise
    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Error al eliminar la tarea"
        )
