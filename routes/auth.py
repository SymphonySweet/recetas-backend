# (para login con Google / Facebook, lo configuraremos luego) basico para login de prueba  
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login():
    return {"token": "fake-jwt-token"}