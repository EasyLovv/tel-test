#!/bin/bash
set -e

if [[ "${DEBUG,,}" = "true" ]]; then
    pip install -e .[dev]
fi

echo "Running command"
exec "$@"
