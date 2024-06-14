from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Vegetables(BaseModel):
    listOfVeges: list[str]


app = FastAPI()


@app.post("/vegetables/")
async def create_item(vegetables: Vegetables):
    return vegetables