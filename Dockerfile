FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache \
    build-base \
    curl

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY pyproject.toml uv.lock* ./

RUN uv venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

COPY . .

RUN uv sync

RUN uv pip install .

RUN pytest

CMD ["python", "src/calculator/calculator.py"]
