import httpx
import pandas
import sqlalchemy
from fastapi import FastAPI
from io import StringIO
import psycopg2

app = FastAPI()


@app.get("/")
async def root():
    async with httpx.AsyncClient() as client:
        csv_response = await client.get(
            "https://data.gov.ru/opendata/7703771271-sportobjects/data-20160714T0856-structure"
            "-20160714T0856.csv?encoding=UTF-8",
            headers={"User-Agent": "SportObjects User API"})
        csv_object = pandas.read_csv(StringIO(csv_response.text))
    return {"data": ""}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
