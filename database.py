import os
import beanie
import motor
import motor.motor_asyncio
from models import Todos
from dotenv import load_dotenv

async def init_db():
    load_dotenv()
    client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('MONGODB_URI'))

    await beanie.init_beanie(database=client.db_name, document_models=[Todos])
