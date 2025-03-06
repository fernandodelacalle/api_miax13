# api_miax13


Para ejecutar con venv
```bash
pip install -r requeriments.txt
```

```bash
uvicorn app:app
```

En el navegador: http://127.0.0.1:8000/docs


# Con docker
```bash
docker-compose build
```

```bash
docker-compose up
```

En el navegador: 
|servico|url|
|--|--|
|API | http://localhost:8080/docs|
|Mongoexpres | http://localhost:33119/|
