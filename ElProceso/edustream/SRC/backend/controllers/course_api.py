"""
API para el modelo Course con FastAPI y MongoDB Atlas.
"""
from fastapi import APIRouter, HTTPException, status
from models.course import Course
from typing import List
from db import get_db, instance_db
import pymongo  # type: ignore  # noqa: F401
import os  # noqa: F401


router = APIRouter(prefix="/courses", tags=["courses"])

@router.get("/", response_model=List[Course])
def get_courses():
    db = get_db(instance_db())
    courses = list(db["course"].find())
    for c in courses:
        if "_id" in c:
            c["_id"] = str(c["_id"])
    return [Course(**c) for c in courses]

@router.post("/", response_model=Course, status_code=status.HTTP_201_CREATED)
def create_course(course: Course):
    db = get_db(instance_db())
    course_dict = course.dict(by_alias=True)
    result = db["course"].insert_one(course_dict)
    course_dict["_id"] = str(result.inserted_id)
    return Course(**course_dict)

@router.get("/{course_id}", response_model=Course)
def get_course(course_id: str):
    db = get_db(instance_db())
    course = db["course"].find_one({"_id": course_id})
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    if "_id" in course:
        course["_id"] = str(course["_id"])
    return Course(**course)

@router.put("/{course_id}", response_model=Course)
def update_course(course_id: str, course: Course):
    db = get_db(instance_db())
    update_data = course.dict(by_alias=True)
    result = db["course"].update_one({"_id": course_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Course not found")
    updated = db["course"].find_one({"_id": course_id})
    if "_id" in updated:
        updated["_id"] = str(updated["_id"])
    return Course(**updated)

@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_id: str):
    db = get_db(instance_db())
    result = db["course"].delete_one({"_id": course_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"success": True, "message": f"Course {course_id} deleted"}

# Explicación:
# - Esta es el controlador para cursos donde se podra realizar lo siguiente:
#   - Listar todos los cursos
#   - Crear un nuevo curso
#   - Obtener un curso por su ID
#   - Actualizar un curso existente
#   - Eliminar un curso
