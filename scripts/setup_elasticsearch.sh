#!/bin/sh
# Setup an Elasticsearch instance through a Docker container

# Help Function
show_help() {
  echo "Setup an Elasticsearch instance through a Docker container"
  echo ""
  echo "Usage: $0 [options]"
  echo ""
  echo "Options:"
  echo "  -h, --help         Display this help message."
}

# Parse command-line options
while [ $# -gt 0 ]; do
  case "$1" in
    -h|--help) # Help
      show_help
      exit 0
      ;;
    *) # Unknown option
      echo "Unknown option: $1."
      show_help
      exit 1
      ;;
  esac
  shift
done

# Verify that the script runs from the correct folder
./scripts/check_working_directory.sh --path "$ROOT_DIRECTORY"

# Check if Docker is installed
if command -v docker > /dev/null 2>&1 ; then
    echo "Docker is installed. Version:"
    docker --version
    echo
else
    echo "Docker is not installed. Please install Docker before running this script."
    echo
fi