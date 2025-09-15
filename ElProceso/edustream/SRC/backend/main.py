
import json
from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models.course import Course
from models.lesson import Lesson
from models.user import User
from controllers import user_api as user_controller
from typing import List, Dict, Any
from config.db import get_db, instance_db

courses = []
lessons = []
users = []

templates = Jinja2Templates(directory="public")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
def create_collection(db, name: str) -> Dict[str, Any]:
    try:
        if not db:
            return {"success": False, "error": "Invalid database"}
        if name not in db.list_collection_names():
            db.create_collection(name)
        return {"success": True, "message": f"Collection '{name}' created or already exists."}
    except Exception as e:
        return {"success": False, "error": str(e)}

def insert_initial_data(db, courses: List[Dict], lessons: List[Dict], users: List[Dict]) -> Dict[str, Any]:
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

###########################################

# Endpoint para registro de usuario
@app.post("/registro")
async def registro_post(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    user = User(username=username, email=email, password=password)
    user_controller.create_user(user)
    return RedirectResponse("http://localhost:8001/login", status_code=303)



# Inicialización de la base de datos
if __name__ == "__main__":
    print(main_db())