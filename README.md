# Python Development Template

A Cookiecutter-based template for Python application development. It has been designed to serve as a foundation for DevOps workflows and to streamline development process.

## Main Features

- __Automated Project Setup__: Configures ready-to-use workspace with essential tools and dependencies.
- __Clear Project Structure__: Provides a clearly structured, readable layout that encourages modularity and simplifies CI processes.
- __VSCode .devcontainer__: Preconfigured for development in isolated containers.
- __UV__: Virtual environment management.
- __Pre-commit Hooks__: Automated checks to enforce code quality standards.
- __Tox for Testing__: Automated environment creation and test execution across multiple configurations.
- __Continuous Integration (CI) Workflows__: CI configurations with GitHub Actions for building and pushing Docker images and building, and publishing Python wheels.

### Setting Up Secrets for Docker Hub

To enable Docker Hub authentication in your workflows, you need to add your Docker Hub credentials as secrets in your GitHub repository:

1. Go to your GitHub repository.
2. Click on "Settings".
3. In the "Security" section of the sidebar, click "Secrets and variables" and then "Actions".
4. Click "New repository secret".
5. Add the following secrets:
   - `DOCKER_USERNAME`: Your Docker Hub username.
   - `DOCKER_PASSWORD`: Your Docker Hub password or access token.

Once these secrets are added, the workflows will be able to authenticate with Docker Hub to push images.

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
