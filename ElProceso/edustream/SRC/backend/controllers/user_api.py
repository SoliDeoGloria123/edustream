"""
API para el modelo User con FastAPI y MongoDB Atlas, funcional y tipado.
"""
from fastapi import APIRouter, HTTPException, status
from models.user import User
from typing import List
from config.db import get_db, instance_db

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[User])
def get_users():
    db = get_db(instance_db())
    users = list(db["user"].find())
    for u in users:
        if "_id" in u:
            u["_id"] = str(u["_id"])
    return [User(**u) for u in users]

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    db = get_db(instance_db())
    user_dict = user.dict(by_alias=True)
    if "_id" in user_dict and user_dict["_id"] is None:
        del user_dict["_id"]
    result = db["user"].insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return User(**user_dict)

@router.get("/{user_id}", response_model=User)
def get_user(user_id: str):
    db = get_db(instance_db())
    user = db["user"].find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if "_id" in user:
        user["_id"] = str(user["_id"])
    return User(**user)

@router.put("/{user_id}", response_model=User)
def update_user(user_id: str, user: User):
    db = get_db(instance_db())
    update_data = user.dict(by_alias=True)
    result = db["user"].update_one({"_id": user_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    updated = db["user"].find_one({"_id": user_id})
    if "_id" in updated:
        updated["_id"] = str(updated["_id"])
    return User(**updated)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    db = get_db(instance_db())
    result = db["user"].delete_one({"_id": user_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"success": True, "message": f"User {user_id} deleted"}

@router.post("/authenticate", response_model=User)
def authenticate_user(username: str, password: str):
    db = get_db(instance_db())
    user = db["user"].find_one({"username": username, "password": password})
    if not user:
        return None
    if "_id" in user:
        user["_id"] = str(user["_id"])
    return User(**user)
