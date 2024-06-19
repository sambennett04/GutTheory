from collections import Counter
from typing import List, Dict
from ..util.string_util import StringUtil

#this file calculates the distinct amount of fruits and veggies in a list and then calculates if that number is gte 30
class FoodAnalyzer(object):
    foods: List[str]
    inputLength: int #what does this do
    distribution: Dict[str, int] 
    distinctCount: int
    distinctCountGteThirty: bool

    def __init__(self, foods:List[str]) -> object:

        self.foods = StringUtil.clean_list(foods)
        self.distribution = dict(Counter(foods)) #creates a dictionary that has a name of a fruit as a key and the number of times that fruit occurs in the foods list as a value
        keys = self.distribution.keys() #finds the number of distinct fruits/vegetables using the keys of self.distribution
        self.distinctCount = len(keys)
        self.distinctCountGteThirty = self.distinctCount >= 30
        self.inputLength = sum([self.distribution[key] for key in keys]) #what does this do   