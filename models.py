from beanie import Document
from pydantic import Field
from datetime import datetime

class Todos(Document):
    todo: str = Field(max_length=400)
    isDone: bool = False
    date_created: datetime = datetime.now()

    class Settings:
        name = 'todo_db'

    class Config:
        json_schema_extra = {
            "todo": "A sample todo",
            "isDone": "False",
            "date_created": datetime.now(),
        }
