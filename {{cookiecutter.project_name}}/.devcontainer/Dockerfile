FROM python:3.11-slim-buster

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get -y install curl git build-essential && \
    pip install --upgrade pip

RUN pip install poetry && \
    poetry config virtualenvs.in-project true 

RUN poetry self add poetry-bumpversion

ENV PYTHONPATH="/workspaces/{{cookiecutter.package_name}}/src"

