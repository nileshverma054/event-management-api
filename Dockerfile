FROM python:3.12-slim as builder

RUN pip install poetry==1.8.3

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache


WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN poetry install && rm -rf $POETRY_CACHE_DIR

# --- final

FROM python:3.12-slim as final

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
