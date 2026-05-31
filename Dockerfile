FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .

RUN pip install uv

RUN uv sync

COPY . .

CMD ["uv", "run", "celery", "-A", "backend.services.celery_service:celery_app", "worker", "--pool=solo", "--loglevel=info"]