"""
API para el modelo Lesson con FastAPI y MongoDB Atlas.
"""
from fastapi import APIRouter, HTTPException, status
from SRC.backend.models.lesson import Lesson
from typing import List
from SRC.backend.main import get_db, instance_db

router = APIRouter(prefix="/lessons", tags=["lessons"])

@router.get("/", response_model=List[Lesson])
def get_lessons():
    db = get_db(instance_db())
    lessons = list(db["lesson"].find())
    for l in lessons:
        if "_id" in l:
            l["_id"] = str(l["_id"])
    return [Lesson(**l) for l in lessons]  # noqa: E741

@router.post("/", response_model=Lesson, status_code=status.HTTP_201_CREATED)
def create_lesson(lesson: Lesson):
    db = get_db(instance_db())
    lesson_dict = lesson.dict(by_alias=True)
    result = db["lesson"].insert_one(lesson_dict)
    lesson_dict["_id"] = str(result.inserted_id)
    return Lesson(**lesson_dict)

@router.get("/{lesson_id}", response_model=Lesson)
def get_lesson(lesson_id: str):
    db = get_db(instance_db())
    lesson = db["lesson"].find_one({"_id": lesson_id})
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    if "_id" in lesson:
        lesson["_id"] = str(lesson["_id"])
    return Lesson(**lesson)

@router.put("/{lesson_id}", response_model=Lesson)
def update_lesson(lesson_id: str, lesson: Lesson):
    db = get_db(instance_db())
    update_data = lesson.dict(by_alias=True)
    result = db["lesson"].update_one({"_id": lesson_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Lesson not found")
    updated = db["lesson"].find_one({"_id": lesson_id})
    if "_id" in updated:
        updated["_id"] = str(updated["_id"])
    return Lesson(**updated)

@router.delete("/{lesson_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lesson(lesson_id: str):
    db = get_db(instance_db())
    result = db["lesson"].delete_one({"_id": lesson_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return {"success": True, "message": f"Lesson {lesson_id} deleted"}

# Explicación:
# - Esta es el controlador para lecciones donde se podra realizar lo siguiente:
#   - Listar todas las lecciones
#   - Crear una nueva lección
#   - Obtener una lección por su ID
#   - Actualizar una lección existente
#   - Eliminar una lección
