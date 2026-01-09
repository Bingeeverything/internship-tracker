from fastapi import FastAPI
from app.db import get_conn

app = FastAPI()

@app.get("/health")
def health():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            cur.fetchone()
    return {"status": "ok"}