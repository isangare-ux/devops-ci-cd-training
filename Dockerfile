FROM python:3.10-slim

WORKDIR /app

# Requirements kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Restlichen Code kopieren
COPY . .

# Standard-Startkommando
CMD ["python", "src/app.py"]
