# Start with a slim Python 3.9 image
FROM python:3.9-slim-buster

# Update existing system packages
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get -y install git

# Install poetry, a package manager for Python
# Configuring poetry to create virtual environments within the project directory
RUN pip install poetry && \
    poetry config virtualenvs.in-project true && \
    # This plugin helps manage versioning of your Python projects
    poetry self add poetry-bumpversion
