# Here's where you'll make your API server
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel


class Fruit(BaseModel):
    name: str
    season: Optional[list[str]] = None
    sweetness: int
    color: str = "red"
    
class User(BaseModel):
    name: str
    favorite_fruit: Fruit


fruits: list[Fruit] = [
        Fruit(name="Apple",season=["summer", "fall"], sweetness=7),
        Fruit(name="Banana",season=["summer", "fall", "winter", "spring"], sweetness=6),
        Fruit(name="Orange",season=["summer", "fall", "winter", "summer"], sweetness=7),
        ]

users: list[User] = [
        User(name="Jack", favorite_fruit=fruits[0]),
        User(name="Coby", favorite_fruit=fruits[1]),
]

app = FastAPI()

@app.get("/")
async def root():
    return "Hello, World!"

@app.get("/users")
async def get_users():
    return users

@app.get("/favorite_fruit/{name}")
async def favorite_fruit(name: str):
    for user in users:
        if user.name.lower() == name.lower():
            return user.favorite_fruit
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"name {name} was not found"
            )
