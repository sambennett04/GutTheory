from sqlalchemy.orm import Session

from . import schemas

from models import PlantFoods

def get_food(db: Session, food_name: str):
    return db.querry(PlantFoods).filter(PlantFoods.food_name == food_name).first()

