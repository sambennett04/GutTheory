from sqlalchemy import Column, Integer, String
#from sqlalchemy.orm import relationship

from .database import Base

class PlantFoods(Base):
    __tablename__ = "plant_foods"
    __table_args__ = {"schema": "dbo"}

    food_id = Column(Integer, primary_key=True)
    food_name = Column(String(256), unique=True, nullable=False)
    food_kind = Column(String(256), nullable=False)

    
