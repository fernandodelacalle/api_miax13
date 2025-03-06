import os

from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()


client = MongoClient(os.getenv('MONGO_CNX'))

db = client['db_api']
col = db['nombres']


@app.get("/names")
def names():
    names_list = col.find({}, {"_id": 0, "name": 1})
    return [name['name'] for name in names_list]


@app.post("/name")
def name(
    name: str,
    phone: int,
):
    print(f'call with {name}')
    col.insert_one(
        {'name': name, 'phone': phone}
    )
    return {'name': name}

