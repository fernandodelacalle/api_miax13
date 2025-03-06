from fastapi import FastAPI

app = FastAPI()


@app.get("/names")
def names():
    return ['fer', 'jose', 'juan', 'pedro', 'luis', 'maria', 'ana']


@app.post("/name")
def name(name: str):
    return {'name': name}

