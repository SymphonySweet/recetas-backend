from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Conectarse a MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client["recipe_db"]

# Colecciones
users = db.users
recipes = db.recipes
ingredients = db.ingredients
mealplans = db.mealplans

# Datos de ejemplo
user_data = {
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "provider": "google",
    "provider_id": "google123"
}

recipe_data = {
    "title": "Tallarines con salsa boloñesa",
    "description": "Una receta clásica italiana con carne molida.",
    "ingredients": ["Tallarines", "Carne molida", "Tomate", "Cebolla"],
    "instructions": "Hervir la pasta. Cocinar la carne. Mezclar con salsa.",
    "created_by": "juan@example.com"
}

ingredient_data = {
    "name": "Carne molida",
    "quantity": "500g"
}

mealplan_data = {
    "user_email": "juan@example.com",
    "recipes": ["Tallarines con salsa boloñesa"],
    "day": "Lunes"
}

# Insertar datos si no existen
if users.count_documents({"email": user_data["email"]}) == 0:
    users.insert_one(user_data)

if recipes.count_documents({"title": recipe_data["title"]}) == 0:
    recipes.insert_one(recipe_data)

if ingredients.count_documents({"name": ingredient_data["name"]}) == 0:
    ingredients.insert_one(ingredient_data)

if mealplans.count_documents({"day": mealplan_data["day"]}) == 0:
    mealplans.insert_one(mealplan_data)

print("✅ Datos de ejemplo insertados correctamente.")