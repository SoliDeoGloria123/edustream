"""
Seeder para poblar la base de datos EduStream Pro con datos demo.
"""
import os
import pymongo
from dotenv import load_dotenv
from datetime import datetime
from SRC.backend.models.user import User
from SRC.backend.models.course import Course
from SRC.backend.models.lesson import Lesson

# Cargar variables de entorno desde .env
load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))
MONGO_URI = os.getenv("MONGO_URI")

client = pymongo.MongoClient(MONGO_URI)
db = client["EDUSTREAM"]

# Datos demo
now = datetime.now().isoformat()
users = [
    User(username="admin", email="admin@example.com", password="123456", role="admin", created_at=now, updated_at=now).model_dump(by_alias=True),
    User(username="student1", email="student1@example.com", password="123456", role="student", created_at=now, updated_at=now).model_dump(by_alias=True)
]
courses = [
    Course(title="Curso de Python", description="Aprende Python desde cero", category="programacion", created_at=now, updated_at=now).model_dump(by_alias=True),
    Course(title="Curso de React", description="React para principiantes", category="frontend", created_at=now, updated_at=now).model_dump(by_alias=True)
]
lessons = [
    Lesson(course_id="1", title="Introducción a Python", content="Bienvenido al curso", order=1, created_at=now, updated_at=now).model_dump(by_alias=True),
    Lesson(course_id="2", title="Introducción a React", content="Bienvenido al curso", order=1, created_at=now, updated_at=now).model_dump(by_alias=True)
]

def remove_null_id(items):
    for item in items:
        if '_id' in item and item['_id'] is None:
            del item['_id']
    return items

def seed():
    print("Insertando usuarios demo...")
    db["user"].delete_many({})
    db["user"].insert_many(remove_null_id(users))
    print("Insertando cursos demo...")
    db["course"].delete_many({})
    db["course"].insert_many(remove_null_id(courses))
    print("Insertando lecciones demo...")
    db["lesson"].delete_many({})
    db["lesson"].insert_many(remove_null_id(lessons))
    print("✅ Base de datos poblada con datos demo.")

if __name__ == "__main__":
    seed()
