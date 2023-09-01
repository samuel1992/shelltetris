#!/bin/sh

echo "\nChecking coverage for Python code\n"

python -m pytest --cov-report term-missing --cov=. .
