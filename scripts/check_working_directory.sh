#!/bin/sh
# Verify whenever you are working from the corrected passed directory

# Help Function
show_help() {
  echo "Usage: $0 [options]"
  echo "Options:"
  echo "  -h, --help         Display this help message."
  echo "  -p, --path PATH    Specify the path for the script. (Required)"
}

# Parse command-line options
while [ $# -gt 0 ]; do
  case "$1" in
    -h|--help)
      show_help
      exit 0
      ;;
    -p|--path)
      shift
      path="$1"
      ;;
    *)
      echo "Unknown option: $1."
      show_help
      exit 1
      ;;
  esac
  shift
done

echo "Checking the provided path."

if [ -z "$path" ]; then
  echo "Error: Please provide a path using the -p or --path option."
  show_help
  exit 1
fi

echo "Checking working directory..."

# Retrieve current working directory
directory_name=$(basename "$(pwd)")

echo "Working in the directory: ${directory_name}."

if [ ! "$directory_name" = "$path" ]; then
  echo "Error: Must run from '$path' folder."
  exit 1
else
  echo "The working directory is correct."
  exit 0
fi