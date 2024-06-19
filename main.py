from fastapi import FastAPI
import uvicorn
from api import router
### second commit###
api=FastAPI()
@api.get("/api")
def root():
    return{"Welcome to FastAPI"}

@api.get("/api/add")
def add(x:int=10,y:int=20):
    z=x+y
    return{'x':x,
            'y':y,
            "addition result":z}

@api.get("/api/sub")
def add(x:int,y:int):
    z=x-y
    return{"Substraction result":z}
api.include_router(router)

if __name__=="__main__":
    uvicorn.run(api,host="127.0.0.1",port = 8080)