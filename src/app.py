from fastapi import FastAPI

app = FastAPI()

# from pymongo import MongoClient
# client = MongoClient("mongodb://root:example@mongo:27017")
# db = client['mi_collccion']
# col = db['test_col']
# col.insert_one(
#     {'name':'test', 'sadg': 2, 'sg': 3}
# )

@app.get("/names")
def names():
    print('call names')
    return ['fernando', 'jose', 'juan', 'pedro', 'luis', 'maria', 'ana']


@app.post("/name")
def name(name: str):
    print(f'call with {name}')
    return {'name': name}

