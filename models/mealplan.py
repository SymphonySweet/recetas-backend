from pydantic import BaseModel
from typing import List

class MealPlan(BaseModel):
    name: str
    days: List[str]
    recipes: List[str]