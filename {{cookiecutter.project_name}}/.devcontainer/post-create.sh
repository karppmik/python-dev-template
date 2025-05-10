#!/bin/bash

hatch env create && hatch env run pip install -e .
hatch run pre-commit install
