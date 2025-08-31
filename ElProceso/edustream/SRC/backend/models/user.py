"""
Modelo de Usuario para EduStream Pro
"""
from typing import Optional, List
from pydantic import BaseModel, Field

class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    email: str
    password: str  # Hasheada
    role: str  # 'admin' o 'student'
    last_login: Optional[str] = None
    is_active: bool = True
    courses_enrolled: List[str] = []  # IDs de cursos
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
