FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/api/lists/*

COPY requiements.txt .
RUN pip install --no-cache -r requiements.txt

COPY . .
