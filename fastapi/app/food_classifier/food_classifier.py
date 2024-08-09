from os import path
from typing import List 
from dataclasses import dataclass
import pathlib
from ..util.string_util import StringUtil

#this file returns a list full of FoodClassificationResult objects which, after digesting a user inputed list of foods, contain the name of the food item and the classification of that item 

@dataclass
class FoodClassificationResult:
    name = ""
    type = ""

class FoodClassifier(object): #these "codes" ensure that classification throughout code is uniform for fruits/veggies and other
    VEGGIE_CODE = "vegetable"
    FRUIT_CODE = "fruit"
    NULL_CODE = "niether fruit nor vegetable"

    def __init__(self) -> object:

        #__file__ means the current file: Meaning the food_classifier.py file
        #so this returns the file path of the parent of the current file to the variable executingPath

        executingPath = pathlib.Path(__file__).parent.resolve()  
        veggiePath = path.join(executingPath, "resources","vegetable.txt") #these two path.join methods make sure that no matter what file organization system the machine running this code uses, the code will be able to access the correct file
        fruitPath = path.join(executingPath, "resources", "fruit.txt")
        self._fruits = set(FoodClassifier.read_text(fruitPath)) #creating sets with names of possible fruits/veggies to compare the user inputted list to
        self._veggies = set(FoodClassifier.read_text(veggiePath))

    def read_text(filePath: str) -> List[str]: #read the fruit.txt and veggie.txt files and turn them into cleaned lists
        
        items = []

        with open(filePath, "r") as f:
            items = f.readlines()
            items = StringUtil.clean_list(items)

        return items

    def classify_foods(self, listOfFoods: List[str]) -> List[FoodClassificationResult]:
        classifiedList = []
        
        for v in listOfFoods:
            
            upperV = StringUtil.clean_string(v)
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