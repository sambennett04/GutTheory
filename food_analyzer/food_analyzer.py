from collections import Counter
from typing import List, Dict

class FoodAnalyzer(object):
    foods: List[str]
    inputLength: int
    distribution: Dict[str, int]
    distinctCount: int
    distinctCountGteThirty: bool

    def __init__(self, foods:List[str]) -> object:

        self.foods = [e.upper().strip() for e in foods]
        self.distribution = dict(Counter(foods))
        keys = self.distribution.keys()
        self.distinctCount = len(keys)
        self.distinctCountGteThirty = self.distinctCount >= 30
        self.inputLength = sum([self.distribution[key] for key in keys])        