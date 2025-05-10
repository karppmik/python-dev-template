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

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:$PATH"

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml README.md ./

COPY src/{{cookiecutter.package_name}} /src/{{cookiecutter.package_name}}

WORKDIR /src

RUN uv pip install --link-mode=copy --editable ".[dev]"

ENV PYTHONPATH="/src"

ENTRYPOINT ["python3"]
