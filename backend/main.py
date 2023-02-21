# Here's where you'll make your API server
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel

class Fruit(BaseModel):
    name: str
    season: Optional[list[str]] = None
    sweetness: int
    color: str = "red"

fruits: list[Fruit] = [
        Fruit(name="Apple",season=["summer", "fall"], sweetness=7),
        Fruit(name="Banana",season=["summer", "fall", "winter", "spring"], sweetness=6),
        Fruit(name="Orange",season=["summer", "fall", "winter", "summer"], sweetness=7),
        ]

app = FastAPI()

@app.get("/")
async def root():
    return "Hello, World!"

@app.get("/fruits")
async def get_fruits():
    return fruits

@app.get("/favorite_fruit/{name}")
async def favorite_fruit(name: str):
    if name.lower() == "jack":
        return "apples"
    elif name.lower() == "coby":
        return "banana"
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"name {name} was not found"
                )
