from fastapi import APIRouter
from models.mealplan import MealPlan
from database import db

router = APIRouter(prefix="/mealplans", tags=["Meal Plans"])

@router.post("/")
def create_mealplan(plan: MealPlan):
    db.mealplans.insert_one(plan.dict())
    return {"message": "Plan de comidas creado"}