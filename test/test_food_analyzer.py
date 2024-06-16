import pytest
from os import path
import pathlib
from ..food_analyzer.food_analyzer import FoodAnalyzer

class TestFoodAnalyzer:
    foods = ["beef", "beef", "apple", "pear", "carrot"]

    def test_food_analyzer(self):
        f = FoodAnalyzer(foods=self.foods)
        assert f.distinctCount == 4
        assert f.inputLength == 5
        assert not f.distinctCountGteThirty
        assert f.distribution["beef"] == 2
        assert f.distribution["apple"] == 1
        assert f.distribution["pear"] == 1
        assert f.distribution["carrot"] == 1