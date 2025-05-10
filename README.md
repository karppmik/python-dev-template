# Python Development Template

A Cookiecutter-based template for Python application development. It has been designed to serve as a foundation for DevOps workflows and to streamline development process.

## Main Features

- __Automated Project Setup__: Configures ready-to-use workspace with essential tools and dependencies.
- __Clear Project Structure__: Provides a clearly structured, readable layout that encourages modularity and simplifies CI processes.
- __VSCode .devcontainer__: Preconfigured for development in isolated containers.
- __UV__: Virtual environment management.
- __Pre-commit Hooks with Ruff__: Automated checks to enforce code quality standards.
- __Tox for Testing__: Automated environment creation and test execution across multiple configurations.
- __Continuous Integration (CI) Workflows__: CI configurations with GitHub Actions for:
  - **Docker Build and Push**: Automates the building and pushing of Docker images to a container registry.
  - **Package Build**: Automates the building and publishing of Python wheels to a package index.

## Usage

Install Cookiecutter from Source:

```bash
git clone https://github.com/cookiecutter/cookiecutter.git
cd cookiecutter
python setup.py install
```

Generate a New Project:

```bash
cookiecutter https://github.com/karppmik/python-dev-template.git
```

## Authors

Mikael Karppinen

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

The MIT License is a permissive open source license that allows for the free use, modification, and distribution of the code, both in commercial and non-commercial projects. It provides limited liability and disclaims warranties of any kind. Please refer to the [LICENSE](LICENSE) file for the full text of the license.
