FROM python:3.13-slim

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        curl \
        git \
        build-essential \
        docker.io \
        gnupg \
        ca-certificates \
        libssl-dev \
        pkg-config && \
    rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PYTHONPATH="/workspaces/{{cookiecutter.package_name}}/src"
