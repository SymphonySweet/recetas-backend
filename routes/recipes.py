from fastapi import APIRouter, HTTPException
from models.recipe import Recipe
from database import db
from bson import ObjectId

router = APIRouter(prefix="/recipes", tags=["Recipes"])

# Crear receta
@router.post("/")
def create_recipe(recipe: Recipe):
    nueva_receta = recipe.dict()

    # Si la imagen está vacía o None, asignar la por defecto
    if not nueva_receta.get("image"):
        nueva_receta["image"] = "assets/img/default.jpg"

    resultado = db.recipes.insert_one(nueva_receta)
    return {
        "message": "Receta agregada correctamente",
        "id": str(resultado.inserted_id)
    }

# Obtener todas las recetas (lista)
@router.get("/")
def get_recipes():
    recetas = []
    for receta in db.recipes.find():
        recetas.append({
            "id": str(receta["_id"]),
            "title": receta.get("title", ""),
            "description": receta.get("description", ""),
            "price": receta.get("price", 0),
            "image": receta.get("image") or receta.get("imagen", "assets/img/default.jpg"),
            "ingredients": receta.get("ingredients", []),
            "steps": receta.get("steps", [])
        })
    return recetas

# Obtener detalle de receta por ID
@router.get("/{recipe_id}")
def get_recipe_by_id(recipe_id: str):
    try:
        receta = db.recipes.find_one({"_id": ObjectId(recipe_id)})
    except:
        raise HTTPException(status_code=400, detail="ID inválido")

    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")

    return {
        "id": str(receta["_id"]),
        "title": receta.get("title", ""),
        "description": receta.get("description", ""),
        "price": receta.get("price", 0),
        "image": receta.get("image") or receta.get("imagen", "assets/img/default.jpg"),
        "ingredients": receta.get("ingredients", []),
        "steps": receta.get("steps", [])
    }
    
# Eliminar receta por ID
@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: str):
    try:
        resultado = db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    except:
        raise HTTPException(status_code=400, detail="ID inválido")

    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Receta no encontrada")

    return {"message": "Receta eliminada correctamente"}



