FROM python:3.13

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        apt-utils \
        openssh-client \
        curl \
        git \
        build-essential \
        docker.io \
        gnupg \
        ca-certificates \
        libssl-dev \
        pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh