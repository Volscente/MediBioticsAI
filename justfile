#!/usr/bin/env just --justfile

# Load from '.env' file
set dotenv-load

# List available commands
help:
    @just --justfile {{justfile()}} --list --unsorted

# PyLint
lint:
  poetry run pylint --load-plugins pylint_pytest \
  --output-format=colorized \
  --msg-template='Rule: {msg_id} - Position: [{line},{column}] -  {msg}' \
  ./src

# Test .env file
test_env_file:
  echo $TEST_ENV_VAR