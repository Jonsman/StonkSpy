# 1. Nutze ein leichtgewichtiges Python-Image
FROM python:3.11-slim

# 2. Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# 3. Abhängigkeiten kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Den restlichen Code kopieren
COPY . .

# 5. Port 8080 freigeben (Standardport für Cloud Run)
EXPOSE 8080

# 6. Gunicorn starten
# --bind 0.0.0.0:8080 sagt Gunicorn, dass es auf Cloud Run Anfragen hören soll
# main:app bedeutet: Datei main.py, Variable "app"
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "8", "main:app"]