"""
Rutas para el modelo Course con control de acceso por rol.
GET es público, POST/PUT/DELETE solo admin.
"""
from fastapi import APIRouter, Depends, status
from models.course import Course
from controllers.course_api import get_courses, create_course, get_course, update_course, delete_course
from middleware.auth import JWTBearer
from typing import List

router = APIRouter(prefix="/courses", tags=["courses"])

# GET público
@router.get("/", response_model=List[Course])
def route_get_courses():
	return get_courses()

# GET por id público
@router.get("/{course_id}", response_model=Course)
def route_get_course(course_id: str):
	return get_course(course_id)

# POST solo admin
@router.post("/", response_model=Course, status_code=status.HTTP_201_CREATED, dependencies=[Depends(JWTBearer(allowed_roles=["admin"]))])
def route_create_course(course: Course):
	return create_course(course)

# PUT solo admin
@router.put("/{course_id}", response_model=Course, dependencies=[Depends(JWTBearer(allowed_roles=["admin"]))])
def route_update_course(course_id: str, course: Course):
	return update_course(course_id, course)

# DELETE solo admin
@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer(allowed_roles=["admin"]))])
def route_delete_course(course_id: str):
	return delete_course(course_id)
