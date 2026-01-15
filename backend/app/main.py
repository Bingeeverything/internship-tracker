from typing import List, Dict, Any
from fastapi import FastAPI
from app.db import get_conn
from app.models import ApplicationCreate

app = FastAPI()

@app.get("/health")
def health():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            cur.fetchone()
    return {"status": "ok"}


app = FastAPI()

@app.get("/health")
def health():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            cur.fetchone()
    return {"status": "ok"}

@app.post("/applications")
def create_application(payload: ApplicationCreate):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO applications (company, role, link, status, date_applied, notes)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id;
                """,
                (payload.company, payload.role, payload.link, payload.status, payload.date_applied, payload.notes),
            )
            new_id = cur.fetchone()[0]
        conn.commit()
    return {"id": new_id}

@app.get("/applications")
def list_applications() -> List[Dict[str, Any]]:
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, company, role, link, status, date_applied, notes, created_at, updated_at
                FROM applications
                ORDER BY id DESC;
                """
            )
            rows = cur.fetchall()

    results = []
    for r in rows:
        results.append(
            {
                "id": r[0],
                "company": r[1],
                "role": r[2],
                "link": r[3],
                "status": r[4],
                "date_applied": str(r[5]),
                "notes": r[6],
                "created_at": r[7].isoformat(),
                "updated_at": r[8].isoformat(),
            }
        )
    return results

    return {"status": "ok"}