from pydantic import BaseModel #help with typing for API's, helping you define a data type held within your API
from typing import List 

class Foods(BaseModel):
    listOfFoods: List[str]