from fastapi import APIRouter
from models.recipe import Recipe
from database import db

router = APIRouter(prefix="/recipes", tags=["Recipes"])

@router.post("/")
def create_recipe(recipe: Recipe):
    db.recipes.insert_one(recipe.dict())
    return {"message": "Receta agregada"}