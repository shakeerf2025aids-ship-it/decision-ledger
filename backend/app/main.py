from fastapi import FastAPI

app = FastAPI(title="Decision Ledger", version="0.1.0")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"project": "Decision Ledger", "status": "running"}


@app.get("/health")
def read_health() -> dict[str, str]:
    return {"status": "healthy"}
