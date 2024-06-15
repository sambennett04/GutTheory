from os import path

class foodClassifier():

    def __init__(self):
        self._veggies = None
        self._fruits = None

        veggiePath = path.join("resources","vegetable.txt")
        fruitPath = path.join("resources", "fruit.txt")

        self._fruits = set(foodClassifier.readTxt(fruitPath))
        self._veggies = set(foodClassifier.readTxt(veggiePath))


    def readTxt(t):
        f = open(t, "r")
        items = f.readlines()
        [i.upper() for i in items]
        f.close()

        return items

    def classify_Foods(self, list):
        classifiedList = []
        for v in list:
            upperV = v.upper()
            isVeggie = self.isVegetable(upperV)
            isFruit = self.isFruit(upperV)
            if isVeggie:
                classifiedList.append({"name": v, "type": "vegetabe"})
            elif isFruit:
                classifiedList.append({"name": v, "type": "fruit"})
            else:
                classifiedList.append({"name": v, "type": "not fruit or vegetable"})
        
        return classifiedList

    def isFruit(self, str):
        if (str in self._fruits):
            return True
        else:
            return False

    def isVegetable(self, str):
        if (str in self._veggies):
            return True
        else:
            return False

    