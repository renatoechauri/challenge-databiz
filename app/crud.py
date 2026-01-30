from sqlalchemy.orm import Session
from sqlalchemy import select

from .models import Task
from .schemas import TaskCreate, TaskUpdate


def create_task(db: Session, data: TaskCreate) -> Task:
    task = Task(
        titulo=data.titulo,
        descripcion=data.descripcion,
        completada=data.completada,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def list_tasks(db: Session) -> list[Task]:
    stmt = select(Task).order_by(Task.id.asc())
    return list(db.scalars(stmt).all())


def get_task(db: Session, task_id: int) -> Task | None:
    stmt = select(Task).where(Task.id == task_id)
    return db.scalars(stmt).first()


def update_task(db: Session, task: Task, data: TaskUpdate) -> Task:
    if data.titulo is not None:
        task.titulo = data.titulo
    if data.descripcion is not None:
        task.descripcion = data.descripcion
    if data.completada is not None:
        task.completada = data.completada

    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: Task) -> None:
    db.delete(task)
    db.commit()