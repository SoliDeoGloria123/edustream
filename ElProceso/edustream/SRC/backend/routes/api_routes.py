from controllers.course_api import router as course_router
from controllers.lesson_api import router as lesson_router
from controllers.user_api import router as user_router

from fastapi import APIRouter
router = APIRouter()
router.include_router(course_router, prefix="/courses")
router.include_router(lesson_router, prefix="/lessons")
router.include_router(user_router, prefix="/users")
