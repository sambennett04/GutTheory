from typing import Annotated
from .food_classifier.food_classifier import FoodClassifier
from .food_analyzer.food_analyzer import FoodAnalyzer
from .request_models.input import Foods
from .request_models.output import FoodClassification, IndividualFoodClassification, AnalyzeFoods
from .log.log_config import LogConfig
from .util.constants import Constants 
from fastapi import Depends, FastAPI
from functools import lru_cache
from logging.config import dictConfig
from json import dumps
import logging
from logging import Logger

app = FastAPI()

# read more about LRU cache for managing dependencies 
# here: https://fastapi.tiangolo.com/advanced/settings/#creating-the-settings-only-once-with-lru_cache
# lru cache(a place where you can memoize values and recall them) ensures that we only instantiate a resource/dependency once 
# when a method decorated with @lru_cache runs multiple times it will only 
# return the value that was returned from the first call to the method
@lru_cache
def get_food_classifier():
    return FoodClassifier()

#above is an example of the singleton pattern, which restrcits the instantiation of a class to singular instance

@lru_cache
def get_logger():
    dictConfig(LogConfig().model_dump())
    return logging.getLogger(Constants.APP_NAME)


@app.post("/classify-foods")#you can define structured data in the body of a post request
#Type annotation allows you to retrieve data from the lru cache. Here fetching the instance of FoodClassifier that we are sustaining over the servers run time 
#This is the pattern to use for the typing for fetching something from the lru cache in a fast api end point: Annotated[type of the object, Depends(name of the function that fetches the object from the lru cache)]
async def classify_foods(foods: Foods, classifier: Annotated[FoodClassifier, Depends(get_food_classifier)], logger: Annotated[Logger, Depends(get_logger)]) -> FoodClassification:
    
    # log the length of the input so we can debug potential data 
    # loss between the client and the server
    inputLength = len(foods.listOfFoods)
    logger.info(f"{classify_foods.__name__}: The length of the input list of foods is: {inputLength}")

    classifiedList = classifier.classify_foods(foods.listOfFoods)
    classifiedList = [IndividualFoodClassification(name=e.name, type=e.type) for e in classifiedList] #go over this list comprehension

    # log the length of the output of the classification run so 
    # we can debug potential data loss that results from 
    # classifying foods
    outputLength = len(classifiedList)
    logger.info(f"{classify_foods.__name__}: The length of the processed list is: {outputLength}")

    # dump the output of classification so that it can be studied for
    # optimization and expected behavior
    logger.info(f"{classify_foods.__name__}: Processing result: {dumps([e.__dict__ for e in classifiedList])}")


    foodClassification = FoodClassification(classification=classifiedList)
    
    return foodClassification

@app.post("/analyze-foods")
async def analyze_foods(foods: Foods, logger: Annotated[Logger, Depends(get_logger)]) -> AnalyzeFoods:
    
    # log the length of the input so we can debug potential data 
    # loss between the client and the server
    inputLength = len(foods.listOfFoods)
    logger.info(f"{analyze_foods.__name__}: the length of the input list of foods is: {inputLength}")
    
    foodAnalyzer = FoodAnalyzer(foods.listOfFoods)

    # dump the output of the food analyzer so that it can be studied for
    # optimization and expected behavior
    logger.info(f"{analyze_foods.__name__}: Processing result: {dumps(foodAnalyzer.__dict__)}")


    analyzeFoods = AnalyzeFoods(
        inputLength=foodAnalyzer.inputLength, 
        distinctCount=foodAnalyzer.distinctCount,
        distinctCountGteThirty=foodAnalyzer.distinctCountGteThirty,
        distribution=foodAnalyzer.distribution)
    
    return analyzeFoods
