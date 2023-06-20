import sys
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Optional
from config import engine, SessionLocal
from models.models import Base, Todos
from routers.auth import get_current_user, get_user_exception


sys.path.append('..')
router = APIRouter(
    prefix='/todos',
    tags=['todos'],
    responses={404: {'description': 'Not found'}}
)
Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(
        gt=0, lt=6, description='The priority must be between 1-5')
    complete: bool


@router.get('/')
async def read_all(db: Session = Depends(get_db)):
    return db.query(Todos).all()


@router.get('/user')
async def read_all_by_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    return db.query(Todos).filter(Todos.owner_id == user.get('id')).all()


@router.get('/{todo_id}')
async def read_todo(todo_id: int, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):

    if user is None:
        raise get_user_exception()

    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(
        Todos.owner_id == user.get('id')).first()

    if todo_model is not None:
        return todo_model

    raise http_exception(todo_id)


@router.post('/')
async def create_todo(todo: Todo, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    todo_model = Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    todo_model.owner_id = user.get('id')

    db.add(todo_model)
    db.commit()

    return successful_response(201)


@router.put('/{todo_id}')
async def update_todo(todo_id: int, todo: Todo, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(
        Todos.owner_id == user.get('id')).first()

    if todo_model is None:
        raise http_exception(todo_id)

    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

    return successful_response(201)


@router.delete('/{todo_id}')
async def delete_todo(todo_id: int, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):

    if user is None:
        raise get_user_exception()
    todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(
        Todos.owner_id == user.get('id')).first()

    if todo_model is None:
        raise http_exception(todo_id)
    db.query(Todos).filter(Todos.id == todo_id).delete()
    db.commit()

    return successful_response(200)


def successful_response(status_code: int):
    return {
        'status': status_code,
        'transaction': 'successful'
    }


def http_exception(id=''):
    return HTTPException(status_code=404, detail=f'TOdo {id} not found')
