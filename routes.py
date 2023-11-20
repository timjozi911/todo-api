from typing import List
from models import Todos
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

# get todos
@router.get("/todos")
async def get_all_todos():
    todos = await Todos.find_all().to_list()
    return todos

# fetch a todo
@router.get("/todos/{todo_id}")
def get_todo(todo_id: int) -> List[Todos]:
    return {"data": "fetch a todo"}

# create todo
@router.post("/todos")
def create_todo(todo: Todos):
     return {"data": "create todo"}

# update todo
@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo_new: Todos):
     return {"data": "update todo"}

# delete todo
@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
     return {"data": "delete todo"}