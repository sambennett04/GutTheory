from ...db import schemas, crud
from ..deps import LoggerDep, SessionDep 
from fastapi import APIRouter, HTTPException
from typing import List
from ...request_models.output import AnalyzeFoods, FoodClassificationResult
from ...food_analyzer.food_analyzer import FoodAnalyzer
from ...food_classifier.food_classifier import FoodClassifier
from json import dumps

router = APIRouter()

# test endpoint for orm/database integration. this can be removed when everyone is familiar with 
# integration new capabilities with sqlalchemy and postgres
@router.get("/{food_name}", response_model=schemas.PlantFood)
def read_food(food_name: str, logger: LoggerDep, db: SessionDep):

    '''
    Get a food by name
    '''

    food_name_lower = food_name.strip().lower()

    logger.info(f"{read_food.__name__}: normalized food name is: {food_name_lower}")

    plant_food = crud.get_food(db, food_name=food_name_lower)
    
    if plant_food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    
    return plant_food

# get foods
@router.post("/", response_model=List[schemas.PlantFood])
def read_foods(food_names: List[str], logger: LoggerDep, db: SessionDep):

    '''
    List foods 
    '''

    # normalize food names to lower before passing request to database
    # all string data in the database should be lower case
    food_names_lower = set([name.strip().lower() for name in food_names])

    logger.info(f"{read_foods.__name__}: normalized foods list is: {food_names_lower}")

    # fetch a list of results from the database using an IN filter
    # so that we do not have to make multiple trips
    plant_foods = crud.get_foods(db, food_names=food_names_lower)

    if plant_foods is None:
        raise HTTPException(status_code=404, detail="No foods found matching the input")
    
    return plant_foods

@router.post("/analyze")
async def analyze_foods(foods: List[str], logger: LoggerDep) -> AnalyzeFoods:

    '''
    Analyzes a group of foods for gut health metrics
    '''
    
    # log the length of the input so we can debug potential data 
    # loss between the client and the server
    inputLength = len(foods)
    logger.info(f"{analyze_foods.__name__}: the length of the input list of foods is: {inputLength}")
    
    foodAnalyzer = FoodAnalyzer(foods)

    # dump the output of the food analyzer so that it can be studied for
    # optimization and expected behavior
    logger.info(f"{analyze_foods.__name__}: Processing result: {dumps(foodAnalyzer.__dict__)}")

    analyzeFoods = AnalyzeFoods(
        inputLength=foodAnalyzer.inputLength, 
        distinctCount=foodAnalyzer.distinctCount,
        distinctCountGteThirty=foodAnalyzer.distinctCountGteThirty,
        distribution=foodAnalyzer.distribution)
    
    return analyzeFoods

#you can define structured data in the body of a post request
#Type annotation allows you to retrieve data from the lru cache. Here fetching the instance of FoodClassifier that we are sustaining over the servers run time 
#This is the pattern to use for the typing for fetching something from the lru cache in a fast api end point: Annotated[type of the object, Depends(name of the function that fetches the object from the lru cache)]
@router.post("/classify")
async def classify_foods(food_names: List[str], logger: LoggerDep, db: SessionDep) -> List[FoodClassificationResult]:
    
    # log the length of the input so we can debug potential data 
    # loss between the client and the server
    inputLength = len(food_names)
    logger.info(f"{classify_foods.__name__}: The length of the input list of foods is: {inputLength}")

    # normalize food names to lower before passing request to database
    # all string data in the database should be lower case
    # need to deduplicate list before sending to database
    food_names_lower = set([name.strip().lower() for name in food_names])

    # fetch a list of results from the database using an IN filter
    # so that we do not have to make multiple trips
    plant_foods = crud.get_foods(db, food_names=food_names_lower)

    reconciled_foods = FoodClassifier.reconcile_foods(input_foods=food_names_lower, retrieved_foods=plant_foods)
    
    # log the length of the output of the classification run so 
    # we can debug potential data loss that results from 
    # classifying foods
    output_length = len(reconciled_foods)
    logger.info(f"{classify_foods.__name__}: The length of the processed list is: {output_length}")

    # dump the output of classification so that it can be studied for
    # optimization and expected behavior
    logger.info(f"{classify_foods.__name__}: Processing result: {dumps([e.__dict__ for e in reconciled_foods])}")
    
    return reconciled_foods