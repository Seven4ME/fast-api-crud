FROM python:3.8-slim

RUN apt-get update && \
    apt-get -y install gcc mono-mcs && \
    rm -rf /var/lib/apt/lists/*

RUN pip install poetry
WORKDIR /code
COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

RUN useradd -ms /bin/bash docker_user
USER docker_user

WORKDIR /code
COPY --chown=docker_user src ./src

