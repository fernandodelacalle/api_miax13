from fastapi import FastAPI

app = FastAPI()


@app.get("/names")
def names():
    print('call names')
    return ['fernando', 'jose', 'juan', 'pedro', 'luis', 'maria', 'ana']


@app.post("/name")
def name(name: str):
    print(f'call with {name}')
    return {'name': name}

