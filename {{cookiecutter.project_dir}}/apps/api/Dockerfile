FROM shiti/python-poetry:1.0.0

ENV PATH=/app/.venv/bin:$PATH

WORKDIR /app

COPY apps/api/poetry.lock apps/api/pyproject.toml ./

RUN poetry install

COPY common ../common
COPY ai ../ai
COPY apps/api/ ./api

WORKDIR /app/api

EXPOSE 8080

CMD ["gunicorn", "config.wsgi", "-b", "0.0.0.0:8080"]
