from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

arr = []


class New(BaseModel):
    text: str


@app.get("/test")
async def test():
    return "Information Kapybara"


@app.get("/info")
async def f():
    return arr[0]


@app.post("/new_info")
async def new_info(text: New):
    arr[0] = text.text
    return arr[0]
