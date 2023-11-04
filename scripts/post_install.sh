#!/bin/bash
# This script will be executed as the final step of the dev container build

set -e

pip3 install --user -r requirements/requirements.txt
pip3 install --user -r requirements/requirements-dev.txt
pre-commit install
