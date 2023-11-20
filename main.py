from fastapi import FastAPI
from routes import router
from database import init_db

app = FastAPI()

@app.on_event("startup")
async def connect():
    await init_db()

app.include_router(router)
