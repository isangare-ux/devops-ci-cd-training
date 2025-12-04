FROM python:3.10-slim

WORKDIR /app

# Requirements kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Restlichen Code kopieren
COPY . .

# Port-Dokumentation (für Info, nicht zwingend)
EXPOSE 8000

# FastAPI App mit Uvicorn starten
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
