# {{cookiecutter.project_name}}

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
3. [Development Environment Setup](#development-environment-setup)
   - [Run Container](#run-container)
   - [Git Repository](#git-repository-and-pre-commit-hooks)
   - [Virtual Environment](#virtual-environment)
4. [Authors](#authors)
5. [License](#license)

## Introduction

This documentation describes the basic setup of the project. More in-depth documentation about the usage and workflow will be updated later...

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

### Virtual Environment

Activate virtual environment:

```
poetry shell
```

This command also creates the .venv folder inside the project folder on the first time. In case you run into problems, delete the .venv folder and run the command again.

### Git Repository and Pre-commit Hooks

If you have an existing __empty__ Git repository, initialize Git within the development container. Then install and initialize pre-commit hooks. Finally push the Cookiecutter stubs.

```
git init
git remote add origin REPOURI
git add -A
```

```
pre-commit install
pre-commit run --all-files
```

```
git add -A
git commit -m "Cookiecutter stubs"
git branch -M main
git push origin -u main
```

## Authors

{{cookiecutter.full_name}}

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

The MIT License is a permissive open source license that allows for the free use, modification, and distribution of the code, both in commercial and non-commercial projects. It provides limited liability and disclaims warranties of any kind. Please refer to the [LICENSE](LICENSE) file for the full text of the license.
