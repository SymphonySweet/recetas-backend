from fastapi import APIRouter
from models.recipe import Recipe
from database import db
from bson import ObjectId

router = APIRouter(prefix="/recipes", tags=["Recipes"])

# Crear receta
@router.post("/")
def create_recipe(recipe: Recipe):
    db.recipes.insert_one(recipe.dict())
    return {"message": "Receta agregada"}

# Obtener todas las recetas
@router.get("/")
def get_recipes():
    recetas = []
    for receta in db.recipes.find():
        receta["_id"] = str(receta["_id"])  # Convertir ObjectId a string
        recetas.append(receta)
    return recetas
