from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def ola():
    return {"mensagem": "Hello, World!"}