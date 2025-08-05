from fastapi import APIRouter
from models.user import User
from database import db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(user: User):
    db.users.insert_one(user.dict())
    return {"message": "Usuario creado"}