import os
import pymongo # type: ignore
from dotenv import load_dotenv

# Cargar .env correctamente
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

MONGO_URI = os.getenv("MONGO_URI")

def instance_db():
    try:
        return pymongo.MongoClient(MONGO_URI)
    except Exception as e:
        return {"success": False, "error": str(e)}

def get_db(client):
    if not client:
        return {"success": False, "error": "Invalid MongoDB client"}
    return client["EDUSTREAM"]
