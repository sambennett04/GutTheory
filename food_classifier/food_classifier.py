from os import path
from typing import List 
from dataclasses import dataclass
import pathlib

@dataclass
class FoodClassificationResult:
    name = ""
    type = ""

class FoodClassifier(object):
    VEGGIE_CODE = "vegetable"
    FRUIT_CODE = "fruit"
    NULL_CODE = "niether fruit nor vegetable"

    def __init__(self) -> object:

        executingPath = pathlib.Path(__file__).parent.resolve()
        veggiePath = path.join(executingPath, "resources","vegetable.txt")
        fruitPath = path.join(executingPath, "resources", "fruit.txt")
        self._fruits = set(FoodClassifier.read_text(fruitPath))
        self._veggies = set(FoodClassifier.read_text(veggiePath))

    def read_text(filePath: str) -> List[str]:
        
        items = []

        with open(filePath, "r") as f:
            items = f.readlines()
            items = [i.upper().strip() for i in items]

        return items

    def classify_foods(self, listOfFoods: List[str]) -> List[FoodClassificationResult]:

        classifiedList = []
        
        for v in listOfFoods:
            
            upperV = v.upper()
            isVegetable = self.is_vegetable(upperV)
            isFruit = self.is_fruit(upperV)

            result = FoodClassificationResult()
            result.name = v

            if isVegetable:
                result.type = self.VEGGIE_CODE
                classifiedList.append(result)
            elif isFruit: 
                result.type = self.FRUIT_CODE
                classifiedList.append(result)
            else:
                result.type = self.NULL_CODE
                classifiedList.append(result)
        
        return classifiedList

    def is_fruit(self, food: str) -> bool:
        upperFood = food.upper()
        result = upperFood in self._fruits
        return result

    def is_vegetable(self, food: str) -> bool:
        upperFood = food.upper()
        result = upperFood in self._veggies
        return result