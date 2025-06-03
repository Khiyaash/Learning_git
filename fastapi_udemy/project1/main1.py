from fastapi import FastAPI, Query, Path, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional , Dict
from database import cars

class Car(BaseModel):
    make: str
    model: str
    year: int = Field(..., ge=1970,lt=2022)
    price: float
    engine: Optional[str] = "V4"
    autonomous: bool
    sold: List[str]

app = FastAPI()

@app.get("/")
async def root():
    return {"welcome to api": "fastapi"}

@app.get("/cars", response_model=List[Dict[int, Car]])
async def get_cars(number: int = Query("1", le = 999)):
    response = []
    for id, car in list(cars.items())[:(number)]:
        to_add = {}
        to_add[id] = car
        response.append(to_add)
    return response

@app.get("/cars/{id}", response_model = Car)
async def  get_car_data_by_id(id: int = Path(...,ge=0,lt=100000)):
    car = cars.get(id)
    if not car:
        raise HTTPException( status_code=status.HTTP_404_NOT_FOUND, detail= "could not find the carby id" )
    return car


