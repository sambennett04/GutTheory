from typing import Annotated
from .food_classifier.food_classifier import FoodClassifier
from .food_analyzer.food_analyzer import FoodAnalyzer
from .request_models.input import Foods
from .request_models.output import FoodClassification, IndividualFoodClassification, AnalyzeFoods
from fastapi import Depends, FastAPI
from functools import lru_cache

app = FastAPI()

# read more about LRU cache for managing dependencies 
# here: https://fastapi.tiangolo.com/advanced/settings/#creating-the-settings-only-once-with-lru_cache
# lru cache ensures that we only instantiate a resource/dependency once 
# when a method decorated with @lru_cache runs multiple times it will only 
# return the value returned from the first call to the method
@lru_cache
def get_food_classifier():
    return FoodClassifier()

@app.post("/classify-foods")
async def classify_foods(foods: Foods, classifier: Annotated[FoodClassifier, Depends(get_food_classifier)]) -> FoodClassification:
    classifiedList = classifier.classify_foods(foods.listOfFoods)
    classifiedList = [IndividualFoodClassification(name=e.name, type=e.type) for e in classifiedList]
    foodClassification = FoodClassification(classification=classifiedList)
    
    return foodClassification

@app.post("/analyze-foods")
async def analyze_foods(foods: Foods) -> AnalyzeFoods:
    foodAnalyzer = FoodAnalyzer(foods.listOfFoods)
    analyzeFoods = AnalyzeFoods(
        inputLength=foodAnalyzer.inputLength, 
        distinctCount=foodAnalyzer.distinctCount,
        distinctCountGteThirty=foodAnalyzer.distinctCountGteThirty,
        distribution=foodAnalyzer.distribution)
    
    return analyzeFoods