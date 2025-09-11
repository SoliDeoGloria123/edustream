"""
Rutas para el modelo User con control de acceso por rol.
GET público, POST/PUT/DELETE solo admin.
"""
from fastapi import APIRouter, Depends, status
from models.user import User
from controllers.user_api import get_users, create_user, get_user, update_user, delete_user
from middleware.auth import JWTBearer
from typing import List

router = APIRouter(tags=["users"])

# GET público (puedes cambiar a solo admin si lo prefieres)
@router.get("/", response_model=List[User])
def route_get_users():
	return get_users()

# GET por id público
@router.get("/{user_id}", response_model=User)
def route_get_user(user_id: str):
	return get_user(user_id)

# POST solo admin
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED, dependencies=[Depends(JWTBearer(allowed_roles=["admin"]))])
def route_create_user(user: User):
	return create_user(user)

# PUT solo admin
@router.put("/{user_id}", response_model=User, dependencies=[Depends(JWTBearer(allowed_roles=["admin"]))])
def route_update_user(user_id: str, user: User):
	return update_user(user_id, user)

# DELETE solo admin
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer(allowed_roles=["admin"]))])
def route_delete_user(user_id: str):
	return delete_user(user_id)

@router.post("/api/usuarios/registro", response_model=User, status_code=status.HTTP_201_CREATED)
def registro(user: User):
	return create_user(user)