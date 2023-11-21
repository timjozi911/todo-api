from typing import List
from models import Todos
from fastapi import APIRouter
from beanie import PydanticObjectId

router = APIRouter()

# Hello World
@router.get("/")
def read_root():
    return {"Hello": "World"}

# get todos
@router.get("/todos")
async def get_all_todos() -> List[Todos]:
    todos = await Todos.find_all().to_list()
    return todos

# create todo
@router.post("/todos")
async def create_todo(todo: Todos):
    await todo.create()
    return {"data": "create todo successful"}

# fetch a todo
@router.get("/todos/{todo_id}")
async def get_todo(todo_id: PydanticObjectId) -> Todos:
    todo_to_get = await Todos.get(todo_id)
    return todo_to_get

# update todo
@router.put("/todos/{todo_id}")
def update_todo(todo_id: PydanticObjectId, todo_new: Todos):
     return {"data": "update todo"}

# delete todo
@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: PydanticObjectId):
     return {"data": "delete todo"}