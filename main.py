from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel #help with typing for API's, helping you define a data type held within your API


class Vegetables(BaseModel): #definition of shape of request and manner to validate requests made to the API
    listOfFoods: list[str]

class Foods(BaseModel):
    listOfFoods: list[str]


app = FastAPI()


@app.post("/vegetables/") #change to classifyFood
async def classify_Food(vegetables: Vegetables):
    result = []
    for v in vegetables.listOfFoods:
        if (v[0].lower() == 'c'):
            result.append(v)
    return {"foodsBeginWithTheLetterC": result} #key that describes the data that is being returned from the server

@app.post("/countDistinct")
async def count_Distinct(foods: Foods):
    mySet = set(foods.listOfFoods) 
    gte30 = len(mySet) >= 30
    return {"distinctCount":len(mySet), "overUnder30":gte30}