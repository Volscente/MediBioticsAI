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
  ./src ./tests

# Setup Elasticsearch
setup_elasticsearch:
  bash scripts/setup_elasticsearch.sh

# Create an Elasticsearch user in interactive mode
create_elasticsearch_user:
  bash scripts/create_elasticsearch_user.sh

# Test .env file
test_env_file:
  echo $TEST_ENV_VAR
