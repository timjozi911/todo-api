from models import Todo
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

# get todos
@router.get("/todos")
def get_all_todos():
    pass

# fetch a todo
@router.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    pass

# create todo
@router.post("/todos")
def create_todo(todo: Todo):
    pass

# update todo
@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo_new: Todo):
    pass

# delete todo
@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    pass