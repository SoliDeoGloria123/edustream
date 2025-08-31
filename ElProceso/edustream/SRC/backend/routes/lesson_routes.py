"""
Rutas para el modelo Lesson con control de acceso por rol.
GET es público, POST/PUT/DELETE solo admin.
"""
from fastapi import APIRouter, Depends, status, HTTPException  # noqa: F401
from SRC.backend.models.lesson import Lesson
from SRC.backend.controllers.lesson_api import get_lessons, create_lesson, get_lesson, update_lesson, delete_lesson
from SRC.backend.middleware.auth import JWTBearer
from typing import List

router = APIRouter(prefix="/lessons", tags=["lessons"])

# GET público
@router.get("/", response_model=List[Lesson])
def route_get_lessons():
	return get_lessons()

# GET por id público
@router.get("/{lesson_id}", response_model=Lesson)
def route_get_lesson(lesson_id: str):
	return get_lesson(lesson_id)

# POST solo admin
@router.post("/", response_model=Lesson, status_code=status.HTTP_201_CREATED, dependencies=[Depends(JWTBearer(allowed_roles=["admin"]))])
def route_create_lesson(lesson: Lesson):
	return create_lesson(lesson)

# PUT solo admin
@router.put("/{lesson_id}", response_model=Lesson, dependencies=[Depends(JWTBearer(allowed_roles=["admin"]))])
def route_update_lesson(lesson_id: str, lesson: Lesson):
	return update_lesson(lesson_id, lesson)

# DELETE solo admin
@router.delete("/{lesson_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer(allowed_roles=["admin"]))])
def route_delete_lesson(lesson_id: str):
	return delete_lesson(lesson_id)
