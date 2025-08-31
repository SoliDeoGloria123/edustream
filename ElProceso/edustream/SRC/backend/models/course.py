"""
Modelo de Curso para EduStream Pro
"""
from typing import List, Optional
from pydantic import BaseModel, Field

class Course(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    title: str
    description: str
    category: str
    image_url: Optional[str] = None
    lessons: List[str] = []  # IDs de lecciones
    is_active: bool = True
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
