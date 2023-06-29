#!/bin/bash

# Get the project name from the cookiecutter template
project_name="{{cookiecutter.package_name}}"

# Set the PYTHONPATH environment variable
export PYTHONPATH="/workspaces/${project_name}/src"

poetry lock --no-update
poetry update
poetry install