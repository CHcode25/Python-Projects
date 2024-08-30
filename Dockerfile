FROM python:3.12.4
FROM alpine:latest
EXPOSE 443
WORKDIR /db
WORKDIR /app
COPY roster.db.sqlite /db/
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:443", "app:app","sqlite3", "/data/roster.db.sqlite"]