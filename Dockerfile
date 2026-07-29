FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*
WORKDIR /app

COPY pyproject.toml poetry.lock* ./
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.in-project true && \
    poetry install --only main --no-root

COPY src/ src/

RUN adduser --disabled-password --gecos "" sentimentuser
USER sentimentuser

ENV PYTHONUNBUFFERED=1 MODEL_CACHE_DIR=/app/.model_cache
EXPOSE 8080
CMD ["poetry", "run", "uvicorn", "src.api.main:app", "--port", "8080", "--host", "0.0.0.0"]
