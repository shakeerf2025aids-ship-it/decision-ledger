# Decision Ledger architecture

Phase 1 establishes a Python backend using FastAPI, served by Uvicorn.

The application entry point is `backend/app/main.py`. API routes, models,
schemas, services, AI, memory, and integrations have dedicated directories
under `backend/app/` for future implementation. Backend tests belong in
`backend/tests/`.

The development server can be started from the project root with:

```powershell
..\.venv\Scripts\python.exe -m uvicorn app.main:app --app-dir backend --reload
```
