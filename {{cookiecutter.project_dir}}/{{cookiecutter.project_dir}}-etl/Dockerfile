FROM python

RUN pip install poetry

ENV PATH=/app/.venv/bin:$PATH

WORKDIR /app

COPY poetry.lock ./pyproject.toml ./

RUN poetry install

COPY . ./

CMD ["poetry", "run", "python", "app.py"]
