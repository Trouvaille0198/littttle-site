from typing import List
from fastapi import APIRouter
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from schemas.todo import TodoBase
from models.todo import Todo
from core.db import SessionLocal, engine, get_db
from crud.todo import *


router = APIRouter()


@router.post('/', response_model=TodoBase, tags=['Create a todo'])
def create_todo(todo: TodoBase, db: Session = Depends(get_db)):
    db_todo = crud_get_todo(db, id=todo.id)
    if db_todo:
        raise HTTPException(status_code=400, detail="Todo already exists")
    # return crud_create_todo(db, todo=todo)
    return crud_create_todo(db, todo=todo)


@router.get('/', response_model=List[TodoBase], tags=['Get todos by query'])
def get_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list:
    """
    :param skip: offset
    :param limit: number of todos
    :return: list of todo_schema
    """
    return crud_get_todos(db, skip, limit)


@router.get('/{id}', response_model=TodoBase, tags=['Get todo by id'])
def get_todos(id: int, db: Session = Depends(get_db)):
    db_todo = crud_get_todo(db, id=id)
    if not db_todo:
        raise HTTPException(status_code=400, detail="Todo doesn't exist")
    return db_todo


@router.delete('/{id}', tags=['Delete todo by id'])
def delete_todos(id: int, db: Session = Depends(get_db)):
    db_todo = crud_get_todo(db, id=id)
    if not db_todo:
        raise HTTPException(status_code=400, detail="Todo doesn't exist")
    crud_delete_todo(db, id=id)
    return {"id": id}


@router.put('/{id}', tags=['Update todo wholly'])
def update_todos(id: int, todo: TodoBase, db: Session = Depends(get_db)):
    if id != todo.id:
        raise HTTPException(status_code=400, detail="Todo id dosen't match")
    db_todo = crud_get_todo(db, id=todo.id)
    if not db_todo:
        raise HTTPException(status_code=400, detail="Todo doesn't exist")
    crud_update_todo(db, todo=todo)
    return {"id": id}


# @router.patch('/{id}', response_model=TodoBase, tags=['Update todo partially'])
# def update_todos(id: int, attr: dict, db: Session = Depends(get_db)):
#     db_todo = crud_get_todo(db, id=id)
#     if not db_todo:
#         raise HTTPException(status_code=400, detail="Todo doesn't exist")
#     for key, value in attr.items():
#         db_todo.key = value

#     crud_update_todo(db, todo=todo)
