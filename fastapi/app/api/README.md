# Routes
## What are Routes
Routes can be thought of as channel numbers for API resources. The API as a whole is a tv catalog of API resources and by using each route, one can access a specific channel/resource. Standard practice is to have one file per channel category, ie. if we have routes that deal with the user sign in and sign out process they would all go in one file name "user". Using "verbs" such as post,get and update we can modify or retrieve resources at specific routes. Routes allow developers to efficiently divide traffic to specific aspects of an application. 

## Deps.py
Deps.py contains all of our API's dependencies, object our logic depends on that we di not want to declare more than once. Through dependency injection, we create an object and inject it into our application at start up, so we don't reconstruct it for every request. 

## Food.py
Food.py contains the routes related to food retieveal from database, food classification and food analyzation.

## Catalog.py 
Catalog.py is the file in which we map all routes in our routes folder into our API just following start up

## How to add a new route
1. Create a new file under routes to house your new route

2. Import any requirements your route needs to function and enter:
```Python
router = APIRouter()
```

3. To execute code at your route, enter:
```Python
@router.[yourVerb]("/[yourRouteName]")
[your method declaration]
```
IMPORTANT: be sure to select the correct input and output model for your method

4. Once you have added your method and route, import your route from .route into catalog.py

5. In catalog.py type:
```Python
api_router.include_router(
    [yourRouteFileName].router, prefix="/[yourRouteFileName]", tags=["[yourRouteFileTag]"])
```


