from typing import List, Dict
from pydantic import BaseModel

#talk to phil about output

class IndividualFoodClassification(BaseModel):
    name: str
    type: str

class FoodClassification(BaseModel):
    classification: List[IndividualFoodClassification]

class AnalyzeFoods(BaseModel):
    inputLength: int
    distinctCount: int
    distinctCountGteThirty: bool
    distribution: Dict[str, int]