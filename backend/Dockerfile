FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn pydantic python-jose passlib python-dotenv slowapi

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
