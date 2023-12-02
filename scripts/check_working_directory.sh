#!/bin/sh
# Verify whenever you are working from the corrected passed path

# Help Function
show_help() {
  echo "Verify whenever you are working from the corrected passed path"
  echo
  echo "Usage: $0 [options]"
  echo
  echo "Options:"
  echo "  -h, --help         Display this help message."
  echo "  -p, --path PATH    Specify the path for the script. (Required)"
}

# Parse command-line options
while [ $# -gt 0 ]; do
  case "$1" in
    -h|--help) # Help
      show_help
      exit 0
      ;;
    -p|--path) # Provide Path
      shift
      path="$1"
      ;;
    *) # Unknown option
      echo "Unknown option: $1."
      show_help
      exit 1
      ;;
  esac
  shift
done

echo "Checking the provided path..."

# Check if path option is provided
if [ -z "$path" ]; then
  echo "Error: Please provide a path using the -p or --path option."
  show_help
  exit 1
fi

echo "Checking working directory..."

# Retrieve current working directory
directory_name=$(basename "$(pwd)")

echo "Working in the directory: ${directory_name}."

# Check if the current working directory is equal to path option
if [ ! "$directory_name" = "$path" ]; then
  echo "Error: Must run from '$path' folder."
  echo
  exit 1
else
  echo "The working directory is correct."
  echo
  exit 0
fi