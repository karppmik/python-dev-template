FROM python:3.11-slim-buster

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get -y install --no-install-recommends \
        curl \
        git \
        build-essential && \
    rm -rf /var/lib/apt/lists/* 

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry

COPY pyproject.toml ./ 

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

COPY src/{{cookiecutter.package_name}} /{{cookiecutter.package_name}}

ENV PYTHONPATH "${PYTHONPATH}:/{{cookiecutter.package_name}}"

ENTRYPOINT ["python3"]