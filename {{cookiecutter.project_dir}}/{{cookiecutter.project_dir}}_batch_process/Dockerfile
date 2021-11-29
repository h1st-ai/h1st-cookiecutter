FROM shiti/python-poetry:1.0.0

ENV PATH=/app/.venv/bin:$PATH

WORKDIR /app

COPY poetry.lock ./pyproject.toml ./

RUN poetry install

COPY . ./

CMD ["poetry", "run", "python", "app.py"]
