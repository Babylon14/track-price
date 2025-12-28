"""Сборщик всех роутеров v1"""
from fastapi import FastAPI

app = FastAPI(
    title="API v1",
    description="API price tracker from marketplace v1",
    terms_of_service="",
)

@app.get("/")
async def cmd_hello():
    return {"hello": "hello world!"}

