"""Datenbankanbindung (SQLite über SQLAlchemy)."""

from pathlib import Path

from sqlalchemy import Engine, create_engine, text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Basisklasse für alle ORM-Modelle. Tabellen folgen mit den User Stories."""


def create_db_engine(db_path: Path) -> Engine:
    return create_engine(
        f"sqlite:///{db_path.as_posix()}",
        # FastAPI kann Anfragen in verschiedenen Threads bearbeiten.
        connect_args={"check_same_thread": False},
    )


def init_db(engine: Engine, db_path: Path) -> None:
    """Legt Datenordner, Datenbankdatei und alle bekannten Tabellen an."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(engine)
    # Eine echte Verbindung erzwingt, dass SQLite die Datei sofort anlegt,
    # auch solange noch keine Tabellen definiert sind.
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))


def check_db(engine: Engine) -> bool:
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except Exception:
        return False
