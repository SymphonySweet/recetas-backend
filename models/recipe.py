from pydantic import BaseModel
from typing import List, Optional

class Recipe(BaseModel):
    id: Optional[str]
    title: str
    description: Optional[str]
    ingredients: List[str]
    steps: List[str]
