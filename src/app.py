from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()


client = MongoClient("mongodb://root:example@mongo:27017")

db = client['db_api']
col = db['nombres']


@app.get("/names")
def names():
    print('call names')
    return ['fernando', 'jose', 'juan', 'pedro', 'luis', 'maria', 'ana']


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

