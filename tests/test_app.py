from fastapi import FastAPI
import os
import redis

app = FastAPI()

# Redis-Konfiguration (wird in Docker über ENV gesetzt)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))

# Globale Redis-Client-Instanz
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


def add(a: int, b: int) -> int:
    """Einfache Beispiel-Funktion für CI-Tests und API."""
    return a + b


@app.get("/health")
def health():
    # kleiner Check, ob Redis erreichbar ist
    try:
        r.ping()
        redis_status = "ok"
    except Exception:
        redis_status = "unreachable"

    return {"status": "ok", "redis": redis_status}


@app.get("/add")
def add_endpoint(a: int, b: int):
    result = add(a, b)
    return {"a": a, "b": b, "result": result}


@app.post("/counter/incr")
def incr_counter():
    """
    Erhöht einen Zähler in Redis und gibt den neuen Wert zurück.
    """
    new_value = r.incr("my_counter")
    return {"counter": int(new_value)}


@app.get("/counter")
def get_counter():
    """
    Liefert den aktuellen Counter-Wert aus Redis.
    """
    value = r.get("my_counter")
    if value is None:
        return {"counter": 0}
    return {"counter": int(value)}


def main():
    # Nur für lokalen Aufruf ohne Webserver
    result = add(2, 3)
    print(f"App läuft: 2 + 3 = {result}")


if __name__ == "__main__":
    main()
