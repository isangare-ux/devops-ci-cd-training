from fastapi import FastAPI

app = FastAPI(title="Simple DevOps Demo Service")


# -------------------------------------------------------------------
# Logik-Funktion (wird von API und Tests verwendet)
# -------------------------------------------------------------------

def add(a: int, b: int) -> int:
    """Einfache Beispiel-Funktion für CI-Tests und API."""
    return a + b


# -------------------------------------------------------------------
# API ROUTES
# -------------------------------------------------------------------

@app.get("/")
def root():
    """
    Root-Endpoint, damit / nicht 404 liefert.
    Liefert einfache Statusinformationen.
    """
    return {"message": "Service läuft", "endpoints": ["/health", "/add"]}


@app.get("/health")
def health():
    """Health-Check für Monitoring und K8s-Liveness."""
    return {"status": "ok"}


@app.get("/add")
def add_endpoint(a: int, b: int):
    """
    Addition über URL-Parameter:
    Beispiel: /add?a=2&b=3
    """
    result = add(a, b)
    return {"a": a, "b": b, "result": result}


# -------------------------------------------------------------------
# Lokaler Aufruf (python app.py), NICHT für Uvicorn/Docker
# -------------------------------------------------------------------

def main():
    """Wird nur ausgeführt, wenn das Skript direkt gestartet wird."""
    result = add(2, 3)
    print(f"App läuft lokal: 2 + 3 = {result}")


if __name__ == "__main__":
    main()
