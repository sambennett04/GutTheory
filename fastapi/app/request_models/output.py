from typing import Dict
from pydantic import BaseModel

class FoodClassificationResult(BaseModel):
    name: str
    type: str

class AnalyzeFoods(BaseModel):
    inputLength: int
    distinctCount: int
    distinctCountGteThirty: bool
    distribution: Dict[str, int]