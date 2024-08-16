from sqlalchemy.orm import Session
# we opt to import models instead of classes directly from models
# to remove issues that may arise from schemas and models with 
# the same name
from . import models

def get_food(db: Session, food_name: str):
    return db.query(models.PlantFoods).filter(models.PlantFoods.food_name == food_name).first()
