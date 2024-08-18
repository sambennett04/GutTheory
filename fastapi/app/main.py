from .api.catalog import api_router
from fastapi import FastAPI

app = FastAPI()

# add all routes from route catalog
app.include_router(api_router)