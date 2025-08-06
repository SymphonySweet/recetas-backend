from pydantic import BaseModel
from typing import List, Optional

class Recipe(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    ingredients: Optional[List[str]] = []
    steps: Optional[List[str]] = []  # En vez de instructions
    price: Optional[float] = 0
    image: Optional[str] = "assets/img/default.jpg"  # Cambiado a 'image'
    created_by: Optional[str] = None


