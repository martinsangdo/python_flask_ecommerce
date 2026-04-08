from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate
from app.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(user: UserCreate):
    user_id = user_service.create_user(user.dict())
    return {"id": user_id}

@router.get("/")
def get_users():
    return user_service.get_all_users()

@router.get("/{user_id}")
def get_user(user_id: str):
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(user_id: str):
    user_service.delete_user(user_id)
    return {"message": "Deleted successfully"}