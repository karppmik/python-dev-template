# Python Development Template

A Cookiecutter-based template for Python application development. It has been designed to serve as a foundation for DevOps workflows and to streamline development process.

## Main Features

- __Automated Project Setup__: Configures ready-to-use workspace with essential tools and dependencies.
- __Clear Project Structure__: Provides a clearly structured, readable layout that encourages modularity and simplifies CI processes.
- __VSCode .devcontainer__: Preconfigured for development in isolated containers.
- __UV__: Virtual environment and dependency management.
- __Pre-commit Hooks__: Automated checks to enforce code quality standards.
- __Tox for Testing__: Automated environment creation and test execution across multiple configurations.
- __Continuous Integration (CI) Workflows__: CI configurations with GitHub Actions for:
  - **Docker Build and Push**: Automates the building and pushing of Docker images to a container registry. This workflow is triggered on pushes to the main branch. To enable this workflow, ensure you have Docker Hub credentials set up as secrets in your GitHub repository.
  - **Package Build**: Automates the building and publishing of Python wheels to a package index. This ensures that your package is correctly built and ready for distribution.

## Usage

If you're planning to use Git or Dockerhub, create repositories for both before you start. With Git, you should start with empty repository.

Install Cookiecutter:

```
python3 -m pip install cookiecutter
```

Generate a New Project:

```
cookiecutter https://github.com/karppmik/python-dev-template.git
```

## Authors

Mikael Karppinen

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

The MIT License is a permissive open source license that allows for the free use, modification, and distribution of the code, both in commercial and non-commercial projects. It provides limited liability and disclaims warranties of any kind. Please refer to the [LICENSE](LICENSE) file for the full text of the license.
