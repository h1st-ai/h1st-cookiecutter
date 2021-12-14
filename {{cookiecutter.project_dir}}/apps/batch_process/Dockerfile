FROM shiti/python-poetry:1.0.0

ENV PATH=/app/.venv/bin:$PATH

WORKDIR /app

COPY apps/batch_process/poetry.lock apps/batch_process/pyproject.toml ./

RUN poetry install

COPY apps/batch_process/ ./

ADD common ./common

ENTRYPOINT ["python", "app.py"]