FROM snakepacker/python:3.8
#Adding user
RUN useradd -ms /bin/bash docker_user

#Install poetry
RUN apt-get update && apt-get install -y curl pip && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | \
 POETRY_HOME=/opt/poetry python3 && \
 cd /usr/local/bin && \
 ln -s /opt/poetry/bin/poetry && \
 poetry config virtualenvs.create false && apt-get autoremove -y curl pip

WORKDIR /code

COPY poetry.lock pyproject.toml /code/

#Install dependencies
RUN poetry install --no-root

USER docker_user

#Copy project w/ specific user
COPY --chown=docker_user src ./src

