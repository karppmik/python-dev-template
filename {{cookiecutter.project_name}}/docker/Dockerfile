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
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml README.md ./

COPY src /src

RUN uv pip install --system --link-mode=copy .

ENV PYTHONPATH="/src"

ENTRYPOINT ["python3"]
