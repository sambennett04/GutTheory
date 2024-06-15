from typing import Union
import foodClassifier

from fastapi import FastAPI
from pydantic import BaseModel #help with typing for API's, helping you define a data type held within your API
from os import path


class Foods(BaseModel):
    listOfFoods: list[str]

def readTxt(t):
    f = open(t, "r")
    items = f.readlines()
    [i.upper() for i in items]
    f.close()

    return items




app = FastAPI()


@app.post("/vegetables/") #change to classifyFood
async def classify_Fruit_Vegetables(foods: Foods):
    classifiedList = foodClassifier.classify_Foods(foods.listOfFoods)
    return {"classifiedFoods": classifiedList} #key that describes the data that is being returned from the server

@app.post("/countDistinct")
async def count_Distinct(foods: Foods):
    mySet = set(foods.listOfFoods) 
    gte30 = len(mySet) >= 30
    return {"distinctCount":len(mySet), "overUnder30":gte30}