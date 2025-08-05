from pydantic import BaseModel
from typing import List, Optional

class Recipe(BaseModel):
    id: Optional[str] = None
    title: str
    description: Optional[str] = None
    ingredients: Optional[List[str]] = []
    steps: Optional[List[str]] = []  # Nuevo nombre en vez de instructions
    price: Optional[float] = 0
    imagen: Optional[str] = "assets/img/default.jpg"
    created_by: Optional[str] = None

