# {{cookiecutter.project_name}}

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Initial Setup](#initial-setup)
   - [Install code command](#install-code-command)
   - [Build and Run the Development Container](#build-and-run-the-development-container)
   - [Git Repository and Pre-commit Hooks](#git-repository-and-pre-commit-hooks)
   - [Add GitHub Secrets for Docker Hub and PyPI](#add-github-secrets-for-docker-hub-and-pypi)
   - [Enabling Github Actions](#enabling-github-actions)
4. [Development Workflow](#development-workflow)
5. [Dependency Management with uv and pyproject.toml](#dependency-management-with-uv-and-pyprojecttoml)
6. [Testing](#testing)
7. [Docker Integration](#docker-integration)
8. [Authors](#authors)
9. [License](#license)

## Introduction

This documentation outlines the setup, usage and workflow conventions for
developing within this project template. It assumes some familiarity with
Docker, Git, Python packaging and VSCode.

## Getting Started

### Prerequisites

- Docker (for .devcontainer)
- Visual Studio Code

### Installation

- [Docker](https://docs.docker.com/get-docker/).

- [VSCode](https://code.visualstudio.com/download).

- __Dev Containers__ extension from VSCode [marketplace](
https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

## Initial Setup

### Install `code` command

Open VSCode.
Press ```Ctrl + Shift + P``` and select __Install 'code' command in PATH__.

### Build and Run the Development Container

After Docker is installed and running, open __Terminal__ on VSCode, navigate to the repository and open it:

```bash
cd {{cookiecutter.project_name}}
code .
```

You should now be prompted to __Reopen in Container__. This opens the project in
the development container. If not press ```Ctrl + Shift + P``` and select
__Remote-Containers: Rebuild and Reopen in Container__.

The development container will be now built and the dependencies installed (it can take a while, if you're doing this for the first time). The initialization sets up the complete development environment. You can run Python files immediately after the container build completes.

### Git Repository and Pre-commit Hooks

If you have an existing __empty__ Git repository, initialize Git within the development container. Then install and initialize [pre-commit hooks](https://pre-commit.com). Finally push the Cookiecutter stubs.

__Initialize Git__:

```bash
git init
git remote add origin <your-repo-url>
git add -A
```

__Setup pre-commit hooks__:

The hooks are specified in the file `pre-commit-config.yaml`. For more information, refer to the documentation in the hook repos listed in the config file.

```bash
pre-commit install
pre-commit run --all-files
```

__Commit and push__:

```bash
git add -A
git commit -m "Cookiecutter stubs"
git branch -M main
git push origin -u main
```

### Add GitHub Secrets for Docker Hub and PyPI

To securely authenticate with Docker Hub and PyPI in GitHub Actions, you must
configure the following secrets in your repository:

1. Navigate to your GitHub repository.
2. Go to __Settings__ → __Secrets and variables__ → __Actions__.
3. Under __Repository secrets__, click __New repository secret__ and add the
   following:

#### Docker Hub

- `DOCKER_USERNAME`: Your Docker Hub username  
- `DOCKER_PASSWORD`: A [Docker Hub access token](https://hub.docker.com/settings/security)
  (recommended) or your Docker Hub password

Used in the `docker-build.yml` workflow.

#### PyPI

- `PYPI_USERNAME`: Your PyPI username  
- `PYPI_PASSWORD`: A [PyPI API token](https://pypi.org/help/#apitoken)
  (recommended)

Used in the `package-build.yml` workflow.

### Enabling Github Actions

There are two template Github Actions workflows:

- `docker-build.yml`
  - Builds the Docker image defined in `/docker/Dockerfile` and pushes it to Docker Hub.
  - Triggered on push to the `main` branch.
  - Requires `DOCKER_USERNAME` and `DOCKER_PASSWORD` to be set in repository secrets.

- `package-build.yml`.
  - Builds a Python wheel using Poetry and publishes it to PyPI.
  - Triggered on push to the `main` branch.
  - Requires `PYPI_USERNAME` and `PYPI_PASSWORD` secrets.

To make the workflows active, rename the files by removing the __.disabled__ ending of the files.

---

## Development Workflow

Follow this workflow to ensure clean, modular, and reproducible development:

1. __Create a feature branch__  
   Use feature branches for all work:

   ```bash
   git checkout -b feature/<short-description>
   ```

2. __Prototype in `/notebooks`__  
   Start by experimenting in Jupyter notebooks under the `notebooks/` directory.  
   See `notebooks/example_notebook.ipynb` as a reference.

3. __Refactor to `/components`__  
   Once stable, extract reusable logic into Python modules under `components/`.  
   See `components/example_component.py` as a pattern.

4. __Build runnable logic in `/scripts`__  
   Compose modular components into executable scripts.  
   See `scripts/example_script.py` for structure.

5. __Pre-commit hooks__  
   Hooks run automatically before each commit. These check formatting, linting, etc.  
   If not already installed, run:

   ```bash
   pre-commit install
   ```

6. __Push your branch__  
   Push your feature branch to remote:

   ```bash
   git push origin feature/<short-description>
   ```

7. __Open a pull request to `main`__  
   Currently, there is no separate branch check workflow. Tests are run before the build in the same workflow.

8. __Merge to `main`__  
   Merging to `main` triggers automated Docker builds or PyPI releases via GitHub Actions.

---

## Dependency Management with `uv` and `pyproject.toml`

This project uses [`uv`](https://github.com/astral-sh/uv) as the primary dependency resolver.
All dependencies are declared in `pyproject.toml`. We do not use `requirements.txt`.

- __Install all dependencies__:

  ```bash
  uv sync
  ```

- __Add a new dependency__:

  ```bash
  uv add <package>
  ```

- __Upgrade a dependency__:

  ```bash
  uv lock --upgrade-package <package>
  ```

- __Remove a dependency__:

  ```bash
  uv remove <package>
  ```

---

## Testing

All testing is run using `tox`. CI executes tests on every push to `main`.

- __Run all tests locally__:

  ```bash
  uv run tox
  ```

- __Run a specific environment (e.g., Python 3.11)__:

  ```bash
  uv run tox -e py311
  ```

> Ensure tests pass locally before opening a pull request.

---

## Docker Integration

All source code and declared dependencies are copied into the Docker image
via the `/docker/Dockerfile`. This enables consistent deployment and reproducible builds.

You can build the image locally for testing purposes:

```bash
docker build -f /workspaces/{{cookiecutter.project_name}}/docker/Dockerfile -t <image-name> /workspaces/{{cookiecutter.project_name}}
```

After the image is built, you can run the container by specifying a script:

```bash
docker run <image-name> src/{{cookiecutter.package_name}}/scripts/example_script.py
```

Or alternatively:

```bash
docker run <image-name> -m {{cookiecutter.package_name}}.scripts.example_script
```

## Authors

{{cookiecutter.full_name}}

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

The MIT License is a permissive open source license that allows for the free use, modification, and distribution of the code, both in commercial and non-commercial projects. It provides limited liability and disclaims warranties of any kind. Please refer to the [LICENSE](LICENSE) file for the full text of the license.
