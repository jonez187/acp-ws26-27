"""Zentrale Konfiguration des Backends."""

import os
from pathlib import Path

BACKEND_DIR = Path(__file__).resolve().parent.parent

# Standardpfad der SQLite-Datei. Kann über die Umgebungsvariable
# RUNNING_COACH_DB_PATH überschrieben werden (z. B. für Tests).
DEFAULT_DB_PATH = BACKEND_DIR / "data" / "running_coach.db"


def get_db_path() -> Path:
    return Path(os.environ.get("RUNNING_COACH_DB_PATH", DEFAULT_DB_PATH))
