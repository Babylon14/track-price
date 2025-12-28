"""ГЛОБАЛЬНАЯ ТОЧКА ВХОДА"""
from fastapi import FastAPI

app = FastAPI(
    title="Price Tracker API v1",
    description="API price tracker from marketplace v1",
    terms_of_service="",
)

@app.get("/")
async def root():
    return {"message": "hello world!"}


