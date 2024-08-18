from typing import Set
from sqlalchemy.orm import Session
from sqlalchemy import func
# we opt to import models instead of classes directly from models
# to remove issues that may arise from schemas and models with 
# the same name
from . import models

def get_food(db: Session, food_name: str):

    # maybe we need to assume that input data is already cleansed by the time it gets 
    # to this part of the application. right now we perform this transformation
    # on the api route and here. probably redundant and slow for large N
    food_name_lower = food_name.strip().lower()

    return db.query(models.PlantFoods) \
        .filter(func.lower(models.PlantFoods.food_name) == food_name_lower) \
        .first()

def get_foods(db: Session, food_names: Set[str]):
    
    # maybe we need to assume that input data is already cleansed by the time it gets 
    # to this part of the application. right now we perform this transformation
    # on the api route and here. probably redundant and slow for large N
    food_names_lower = [name.strip().lower() for name in food_names]

    return db.query(models.PlantFoods) \
        .filter(func.lower(models.PlantFoods.food_name) \
        .in_(food_names_lower)) \
        .all()