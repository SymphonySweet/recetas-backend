from fastapi import APIRouter
from models.recipe import Recipe
from database import db
from bson import ObjectId

router = APIRouter(prefix="/recipes", tags=["Recipes"])

# Crear receta
@router.post("/")
def create_recipe(recipe: Recipe):
    nueva_receta = recipe.dict()

    # Si la imagen está vacía o None, asignar la por defecto
    if not nueva_receta.get("imagen"):
        nueva_receta["imagen"] = "assets/img/default.jpg"

    resultado = db.recipes.insert_one(nueva_receta)
    return {
        "message": "Receta agregada correctamente",
        "id": str(resultado.inserted_id)
    }

# Obtener todas las recetas
@router.get("/")
def get_recipes():
    recetas = []
    for receta in db.recipes.find():
        recetas.append({
            "id": str(receta["_id"]),
            "title": receta.get("title", ""),
            "description": receta.get("description", ""),
            "price": receta.get("price", 0),
            "imagen": receta.get("imagen", "assets/img/default.jpg")
        })
    return recetas

