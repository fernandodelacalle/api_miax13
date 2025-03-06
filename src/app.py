import os

from fastapi import FastAPI, Depends
from pymongo import MongoClient

app = FastAPI()


def get_collection():
    client = MongoClient(os.environ['MONGO_CNX'])
    db = client['db_api']
    return db['nombres']


@app.get("/names")
def names(
    col=Depends(get_collection)
):
    names_list = col.find({}, {"_id": 0, "name": 1})
    return [name['name'] for name in names_list]


@app.post("/name")
def name(
    name: str,
    phone: int,
    col=Depends(get_collection),
):
    print(f'call with {name}')
    col.insert_one(
        {'name': name, 'phone': phone}
    )
    return {'name': name}
