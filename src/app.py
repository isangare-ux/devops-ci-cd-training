from fastapi import FastAPI
import os
import sqlalchemy
from sqlalchemy import text
import redis

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "fastapi_db")
POSTGRES_USER = os.getenv("POSTGRES_USER", "fastapi_user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "secret123")

# PostgreSQL Engine
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = sqlalchemy.create_engine(DATABASE_URL, echo=False, future=True)


app = FastAPI()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


def add(a: int, b: int) -> int:
    return a + b


@app.get("/health")
def health():
    # Redis Check
    try:
        r.ping()
        redis_status = "ok"
    except Exception:
        redis_status = "unreachable"

    # Postgres Check
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        db_status = "ok"
    except Exception:
        db_status = "unreachable"

    return {
        "status": "ok",
        "redis": redis_status,
        "postgres": db_status
    }
