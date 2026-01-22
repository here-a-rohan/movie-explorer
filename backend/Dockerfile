FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

# 🔧 FIX: upgrade pip + increase timeout
RUN pip install --upgrade pip \
 && pip install --no-cache-dir --default-timeout=120 -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
