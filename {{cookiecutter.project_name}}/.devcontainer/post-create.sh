#!/bin/bash

uv venv
uv pip install --link-mode=copy --editable ".[dev]"