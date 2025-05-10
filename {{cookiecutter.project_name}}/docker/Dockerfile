FROM python:3.13-slim

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get -y install --no-install-recommends \
        curl \
        git \
        build-essential && \
    rm -rf /var/lib/apt/lists/* 

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir hatch

COPY pyproject.toml ./ 

RUN hatch env create

COPY src/{{cookiecutter.package_name}} /{{cookiecutter.package_name}}

ENV PYTHONPATH="/workspaces/{{cookiecutter.package_name}}/src"

ENTRYPOINT ["python3"]
