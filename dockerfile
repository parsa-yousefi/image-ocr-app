FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY ./app /app/app

ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y tesseract-ocr


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
