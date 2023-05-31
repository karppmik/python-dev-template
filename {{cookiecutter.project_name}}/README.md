# {{cookiecutter.project_name}}

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Development Environment Setup](#development-environment-setup)
   - [Run Container](#run-container)
   - [Git Repository](#git-repository)
   - [Virtual Environment](#virtual-environment)
5. [Development Container](#development-container)
    - [Docker](#docker)
    - [DevContainer](#devcontainer)
    - [Post-Create Script](#post-create-script)
6. [Pre-commit Hooks](#pre-commit-hooks)
7. [Usage](#usage)
    - [Git Workflow](#git-workflow)
    - [Poetry](#poetry)
8. [Testing](#testing)
9. [Authors](#authors)
10. [License](#license)

## Introduction

Introduction section.

## Getting Started

### Prerequisites

- Docker (for .devcontainer)
- Visual Studio Code

### Installation

Install [Docker](https://docs.docker.com/get-docker/).

Install [VSCode](https://code.visualstudio.com/download).

Install __Dev Containers__ extension from VSCode [marketplace](
https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

## Development Environment Setup

### Run Container

After Docker is installed and running, navigate to the repository and open it in VSCode:

```
cd your-project-name
code .
```

You should now be prompted to __Reopen in Container__. This opens the project in
the development container. If not press ```Ctrl + Shift + P``` and select
__Remote-Containers: Rebuild and Reopen in Container__.

During first time, it takes a while to build the development container.

### Git Repository

If you have an existing __empty__ Git repository, initialize Git within the development container and push the Cookiecutter stubs.

```
git init
git remote add origin REPOURI
git add -A
git commit -m "Cookiecutter stubs"
git branch -M main
git push origin -u main
```

### Virtual Environment

Activate virtual environment:

```
poetry shell
```

This command also creates the .venv folder inside the project folder on the first time. In case you run into problems, delete the .venv folder and run the command again.

## Development Container

This project uses Docker and Visual Studio Code's DevContainer feature for a consistent, reproducible development environment.

### Docker

The `Dockerfile` in this project sets up a Python 3.9 environment on a slim version of the Buster variant of Debian.

It starts by updating all system packages to their latest versions. `git` is then installed for version control needs.

[Poetry](https://python-poetry.org/), a modern packaging and dependency management tool for Python, is also installed. It's configured to create virtual environments within the project's directory. Additionally, the `poetry-bumpversion` plugin is added to help manage the versioning of the Python project.

### DevContainer

The `.devcontainer` directory contains a `devcontainer.json` file that configures the DevContainer environment. When you open the project in Visual Studio Code and have the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension installed, the project will automatically be opened inside the Docker container.

The `devcontainer.json` file has the following settings:

- `"build"` specifies that the Docker image for the container should be built from the `Dockerfile` in the project root.
- `"extensions"` lists the VS Code extensions that should be automatically installed in the DevContainer. These include extensions for Python development and Jupyter notebooks.
- `"settings"` configures project-specific settings, such as arguments for the Pylint linter and settings for the Python language server.
- `"appPort"` specifies that the container should listen on port 8080 for incoming connections.
- `"postCreateCommand"` specifies a script that should be run after the container is created. This script locks, updates, and installs the Python dependencies of the project using Poetry.

To use this setup, make sure you have Docker installed and the Remote - Containers extension for VS Code. Then, simply open the project in VS Code and choose to reopen it in the container when prompted.

### Post-Create Script

The `post-create.sh` script is specified in the `devcontainer.json` file's `"postCreateCommand"` field and is automatically run after the DevContainer has been built. Here's what each command in the script does:

- `poetry lock --no-update`: This command generates a `poetry.lock` file based on the current `pyproject.toml`, without updating the dependencies. The lock file ensures that everyone working on the project uses exactly the same versions of the dependencies.

- `poetry update`: This command updates all dependencies as according to the `pyproject.toml` file. It respects semantic versioning.

- `poetry install`: This command installs the project dependencies. If a `poetry.lock` file is present, it will use the exact versions from there. If not, it will create one based on the `pyproject.toml` file.

Running these commands in the post-create script ensures that the project's dependencies are correctly installed and up-to-date every time the DevContainer is built.

## Pre-commit Hooks

This template uses the following pre-commit hooks:

- `trailing-whitespace`: This hook trims trailing whitespace.
- `end-of-file-fixer`: Ensures that a file is either empty, or ends with one newline.
- `check-yaml`: Checks whether YAML files parse correctly.
- `check-added-large-files`: Prevents you from committing large files. The current maximum file size is 3300KB.
- `black`: An opinionated code formatter that reformats your code to make it more readable and consistent. It's configured to enforce a line length of 88 characters.
- `bandit`: A security linter for Python that checks for common programming errors that might lead to security problems.
- `mypy`: A static type checker for Python, configured to run in strict mode and ignore missing imports.
- `pylint`: A comprehensive Python linter that checks for errors, coding standards, and enforces a coding style.
- `isort`: A Python utility to sort imports alphabetically, and automatically separated into sections.
- `codespell`: A tool to fix common misspellings in text files. It's designed primarily for checking misspelled words in source code.
- `python-safety-dependencies-check`: Checks Python dependencies for known security vulnerabilities.

The hooks come pre-installed as Poetry development dependencies. To use these hooks, run ```pre-commit run --all-files```.

## Usage

### Git Workflow

Create a new feature branch:

```
git checkout -b feature/name
```

After you finish coding, increment version number:

```
poetry version patch
```

Stage files and run pre-commit hooks:

```
git add -A
pre-commit run --all-files
```

Commit changes to feature branch:

```
git commit -m "Message"
git push origin feature/name
```

### Poetry

Poetry is used for managing dependencies. If you require a new package, simply add it using the following command:

```
poetry add package
```

If you want to add a development dependency:

```
poetry add package -G dev
```

Removing package:

```
poetry remove package
```

## Testing

To ensure robust code quality, Tox and Pytest are utilized for implementing unit tests. By default, minimum test coverage is set to 70%.

Run unit tests:

```
tox
```

## Authors

{{cookiecutter.full_name}}

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

The MIT License is a permissive open source license that allows for the free use, modification, and distribution of the code, both in commercial and non-commercial projects. It provides limited liability and disclaims warranties of any kind. Please refer to the [LICENSE](LICENSE) file for the full text of the license.
