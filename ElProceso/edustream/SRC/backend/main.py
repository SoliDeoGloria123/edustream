
import os
import json
import pymongo # type: ignore
from dotenv import load_dotenv
from SRC.backend.models.course import Course
from SRC.backend.models.lesson import Lesson
from SRC.backend.models.user import User
from typing import Any, Dict, List
# Define courses, lessons, users as empty lists or import from a data file if needed
courses = []
lessons = []
users = []

# Cargar .env correctamente
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))


MONGO_URI = os.getenv("MONGO_URI")

def instance_db() -> Any:
    try:
        return pymongo.MongoClient(MONGO_URI)
    except Exception as e:
        return {"success": False, "error": str(e)}

def get_db(client: pymongo.MongoClient) -> dict:
    if not client:
        return {"success": False, "error": "Invalid MongoDB client"}
    return client["EDUSTREAM"]
    
def create_collection(db: Any, name: str) -> Dict[str, Any]:
    try:
        if not db:
            return {"success": False, "error": "Invalid database"}
        if name not in db.list_collection_names():
            db.create_collection(name)
        return {"success": True, "message": f"Collection '{name}' created or already exists."}
    except Exception as e:
        return {"success": False, "error": str(e)}

def insert_initial_data(db: Any, courses: List[Dict], lessons: List[Dict], users: List[Dict]) -> Dict[str, Any]:
    try:
        if isinstance(db, dict) and not db.get("success", True):
            return db
        db["course"].insert_many([Course(**data).dict(by_alias=True) for data in courses]) if courses else None
        db["lesson"].insert_many([Lesson(**data).dict(by_alias=True) for data in lessons]) if lessons else None
        db["user"].insert_many([User(**data).dict(by_alias=True) for data in users]) if users else None
        return {"success": True, "message": "Initial data inserted (if any)"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def main_db() -> str:
    result = [
        create_collection(get_db(instance_db()), "course"),
        create_collection(get_db(instance_db()), "lesson"),
        create_collection(get_db(instance_db()), "user"),
        insert_initial_data(get_db(instance_db()), courses, lessons, users)
    ]
    return json.dumps(result, ensure_ascii=False, indent=2)

# Inicialización de la base de datos
if __name__ == "__main__":
    print(main_db())