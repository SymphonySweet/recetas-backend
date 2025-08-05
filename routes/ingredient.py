from fastapi import APIRouter
from models.ingredient import Ingredient
from database import db

router = APIRouter(prefix="/ingredients", tags=["Ingredients"])

@router.post("/")
def add_ingredient(ingredient: Ingredient):
    db.ingredients.insert_one(ingredient.dict())
    return {"message": "Ingrediente añadido"}