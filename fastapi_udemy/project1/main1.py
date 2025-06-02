from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional

class Car(BaseModel):
    make: Optional[str]
    model: Optional[str]
    year: Optional[int] = Field(...,ge=1970,lt=2022)
    price: Optional[float]
    engine: Optional[str] = "V4"
    autonomous: Optional[bool]
    sold: Optional[List[str]]

app = FastAPI()

@app.get("/")
async def root():
    return {"welcome to api": "fastapi"}


