#!/usr/bin/env just --justfile

# Test Justfile
hello:
  echo "hello world"

# PyLint
lint:
  poetry run pylint --load-plugins pylint_pytest
  --output-format=colorized
  --msg-template='Rule: {msg_id} - Position: [{line},{column}] -  {msg}'
  ./src