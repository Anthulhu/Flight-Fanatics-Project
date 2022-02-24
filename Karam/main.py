from fastapi import FastAPI
from fastapi.param_functions import Body
from pydantic import BaseModel





app = FastAPI()


class POSTY(BaseModel):
    Title : str
    City : str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/create")
def create_post(newposty: POSTY):
    print(newposty)
    return{"message":"succesfull" }
