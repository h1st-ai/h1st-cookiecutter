FROM shiti/python-poetry:1.0.0

ENV PATH=/app/.venv/bin:$PATH

WORKDIR /app

COPY ./poetry.lock ./pyproject.toml ./

RUN poetry install

COPY . ./

EXPOSE 8080

CMD ["gunicorn", "{{cookiecutter.module_name}}.wsgi", "-b", "0.0.0.0:8080"]
