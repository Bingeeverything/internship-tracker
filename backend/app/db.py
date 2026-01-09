import os
import psycopg

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/internship_tracker",
)

def get_conn():
    return psycopg.connect(DATABASE_URL)
