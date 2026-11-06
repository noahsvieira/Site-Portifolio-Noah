from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Portfolio API")
STATIC = Path(__file__).parent / "static"

app.mount("/static", StaticFiles(directory=STATIC), name="static")


@app.get("/api/saude")
def saude() -> dict:
    """Rota de teste: confirma que o servidor está vivo."""
    return {"status": "ok"}


@app.get("/")
def home() -> FileResponse:
    """Entrega a página do portfólio."""
    return FileResponse(STATIC / "index.html")