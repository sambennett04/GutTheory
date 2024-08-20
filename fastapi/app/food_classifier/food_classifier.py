from typing import List, Set
from ..request_models.output import FoodClassificationResult
from ..db.models import PlantFoods

class FoodClassifier(object): 
    # this class returns a list full of FoodClassificationResult objects which, 
    # after digesting a user inputed list of foods, 
    # contain the name of the food item and the classification of that item 
    # these "codes" ensure that classification throughout code is uniform for fruits/veggies and other
    VEGGIE_CODE = "vegetable"
    FRUIT_CODE = "fruit"
    OTHER_CODE = "niether fruit nor vegetable"
    NULL_CODE = "food not available in system"

    @staticmethod
    def reconcile_foods(input_foods: Set[str], retrieved_foods: List[PlantFoods]) -> List[FoodClassificationResult]:

        if not input_foods:
            raise ValueError(f"{input_foods.__qualname__} should not be null or empty.")
        
        if not retrieved_foods:
            raise ValueError(f"{retrieved_foods.__qualname__} shoult not be null or empty.")

        result = []
        available_foods = set([food.food_name for food in retrieved_foods])

        for food in input_foods:
            if food in available_foods:
                target_food = [f for f in retrieved_foods if f.food_name == food][0]
                food_classification = FoodClassificationResult(
                    name=target_food.food_name, 
                    type=target_food.food_kind)
            else:
                food_classification = FoodClassificationResult(
                    name=food, 
                    type=FoodClassifier.NULL_CODE)
            
            result.append(food_classification)
        
        return result