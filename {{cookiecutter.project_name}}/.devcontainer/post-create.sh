#!/bin/bash

poetry lock --no-update
poetry update
poetry install