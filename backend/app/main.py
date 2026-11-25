"""Einstiegspunkt der FastAPI-Anwendung.

Start (aus dem Ordner backend/, virtuelle Umgebung aktiv):
    uvicorn app.main:app --reload
"""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request

from app.config import get_db_path
from app.database import check_db, create_db_engine, init_db


def create_app(db_path: Path | None = None) -> FastAPI:
    resolved_db_path = db_path or get_db_path()

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        engine = create_db_engine(resolved_db_path)
        init_db(engine, resolved_db_path)
        app.state.engine = engine
        yield
        engine.dispose()

    app = FastAPI(title="AI Running Coach API", lifespan=lifespan)

    @app.get("/api/health")
    def health(request: Request) -> dict[str, str]:
        """Test-Endpunkt: prüft, ob Backend und Datenbank erreichbar sind."""
        db_ok = check_db(request.app.state.engine)
        return {"status": "ok", "database": "ok" if db_ok else "error"}

    return app


app = create_app()
