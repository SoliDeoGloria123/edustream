"""
Modelo de Lección para EduStream Pro
"""
from typing import Optional
from pydantic import BaseModel, Field

class Lesson(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    course_id: str
    title: str
    content: str  # Puede ser texto, video, etc.
    order: int
    is_active: bool = True
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
