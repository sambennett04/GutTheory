from pydantic import BaseModel

class PlantFoodBase(BaseModel):
    food_name: str
    food_kind: str 

class PlantFood(PlantFoodBase):
    food_id: int

    class Config:
        orm_mode = True

