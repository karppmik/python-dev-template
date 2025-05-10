FROM python:3.11-slim-buster

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get -y install curl git build-essential && \
    pip install --upgrade pip

RUN pip install uv && \
    uv config virtualenvs.in-project true

ENV PYTHONPATH="/workspaces/{{cookiecutter.package_name}}/src"

