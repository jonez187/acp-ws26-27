# AI Running Coach

Ein KI-gestützter Running Coach, der absolvierte Laufeinheiten analysiert und individuelle Trainingsempfehlungen für die nächsten Einheiten erstellt.

## Projektziel

Ziel des Projekts ist die Entwicklung eines Prototyps, der Läufer*innen dabei unterstützt, ihr Training besser zu verstehen und auf Basis ihrer tatsächlichen Trainingsaktivitäten anzupassen.

Dazu werden Trainingsdaten importiert, ausgewertet und für individuelle Trainingsempfehlungen verwendet.

## Geplante Funktionen

- Import von Laufaktivitäten über FIT-Dateien
- Übersicht über Trainingsumfang und Trainingsintensität
- Analyse und Bewertung absolvierter Trainingseinheiten
- Individuelle Empfehlungen für kommende Laufeinheiten
- Berücksichtigung von Nutzerfeedback

## Technologie

| Bereich | Technik |
|---|---|
| Frontend | React + TypeScript (Vite) |
| Backend | Python, FastAPI |
| Datenbank | SQLite über SQLAlchemy |
| Tests | pytest |

## Projektstruktur

```
├── backend/     FastAPI-Anwendung (app/), Abhängigkeiten
├── frontend/    React-Anwendung
├── docs/        technische Dokumentation
└── tests/       Backend-Tests (pytest)
```

## Lokal starten

**Voraussetzungen:** Python ≥ 3.10, Node.js 20.19+ oder ≥ 22.12

### Einmalig einrichten

```bash
# Backend
cd backend
python -m venv .venv
# Windows:      .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements-dev.txt

# Frontend (in einem zweiten Terminal)
cd frontend
npm install
```

### Starten (je ein Befehl, zwei Terminals)

```bash
# Terminal 1 – Backend (im Ordner backend/, virtuelle Umgebung aktiv)
uvicorn app.main:app --reload

# Terminal 2 – Frontend (im Ordner frontend/)
npm run dev
```

Danach http://localhost:5173 öffnen. Unter „Systemstatus“ sollten Backend und Datenbank mit „ok“ angezeigt werden.

- Das Backend läuft auf http://127.0.0.1:8000, die API-Doku liegt unter http://127.0.0.1:8000/docs.
- Das Frontend leitet alle Anfragen an `/api` an das Backend weiter.
- Die SQLite-Datenbank wird beim ersten Start automatisch unter `backend/data/running_coach.db` angelegt (nicht im Repo). Ein anderer Pfad lässt sich über die Umgebungsvariable `RUNNING_COACH_DB_PATH` setzen.

### Tests

```bash
# im Hauptverzeichnis, virtuelle Umgebung des Backends aktiv
pytest
```

## Dokumentation

Weitere Informationen zum Projekt befinden sich im [GitHub Wiki](../../wiki).

## Projektkontext

Das Projekt entsteht im Rahmen des Agile Co-Creation Project (ACP) im Wintersemester 2026/27.
