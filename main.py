from fastapi import FastAPI
from models import Todo

app = FastAPI()
toDos: Todo = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

# get todos
@app.get("/todos")
def get_todos():
    return {"todos": toDos}

# fetch a todo
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in toDos:
        if todo.id == todo_id:
            return {'todo': todo}
    return {"message": "No todo's found"}

# create todo
@app.post("/todos")
def create_todo(todo: Todo):
    toDos.append(todo)
    return {"message": "Todo has been added"}

# update todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo_new: Todo):
    for todo in toDos:
        if todo.id == todo_id:
            todo.id == todo_id
            todo.task = todo_new.task
            return {'message': 'todo has been updated'}
    return {"message": "todo with that id not found"}

# delete todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in toDos:
        if todo.id == todo_id:
            toDos.remove(todo_id)
            return {'message': 'todo has been deleted'}
    return {"message": "todo with that id not found"}
