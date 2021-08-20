FROM python:3.8.11-slim-buster as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION="1.1.6" \
    POETRY_HOME="/opt/poetry" 

ENV PATH=/app/.venv/bin:$POETRY_HOME/bin:$PATH

RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    curl  \
    build-essential


# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

WORKDIR /app

COPY ./poetry.lock ./pyproject.toml ./

RUN poetry config virtualenvs.in-project true && poetry install

COPY . ./

CMD ["gunicorn", "{{cookiecutter.module_name}}.wsgi", "-b", "0.0.0.0:8080"]
