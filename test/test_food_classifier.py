import pytest
from os import path
import pathlib
from ..food_classifier.food_classifier import FoodClassifier

class TestFoodClassifier:
    foodClassifier = FoodClassifier()
    executingPath = pathlib.Path(__file__).parent.resolve()

    def test_read_text(self):
        filePath = path.join(self.executingPath, "resources", "fruit_list.txt")
        items = FoodClassifier.read_text(filePath)
        assert len(items) > 0

    def test_has_veggies(self):
        assert len(self.foodClassifier._veggies)

    def test_has_fruits(self):
        assert len(self.foodClassifier._fruits)
    
    def test_is_fruit(self):
        result = self.foodClassifier.is_fruit("apple")
        assert result

    def test_is_not_fruit(self):
        result = self.foodClassifier.is_fruit("carrot")
        assert not result
    
    def test_is_vegetable(self):
        result = self.foodClassifier.is_vegetable("carrot")
        assert result
    
    def test_is_not_vegetable(self):
        result = self.foodClassifier.is_vegetable("apple")
        assert not result
    
    def test_classify_foods(self):
        foods = ["apple", "carrot", "beef"]
        result = self.foodClassifier.classify_foods(foods)
        assert result[0].type == FoodClassifier.FRUIT_CODE
        assert result[0].name == "apple"
        assert result[1].type == FoodClassifier.VEGGIE_CODE
        assert result[1].name == "carrot"
        assert result[2].type == FoodClassifier.NULL_CODE
        assert result[2].name == "beef"
   
