#!/bin/sh
# Create a new Elasticsearch user
# Reference guide: https://www.elastic.co/guide/en/elasticsearch/reference/current/users-command.html

# TODO Help Function
# Add the separation between arguments and options
show_help() {
  echo "Create a new Elasticsearch user"
  echo
  echo "Usage: $0 [options]"
  echo ""
  echo "Options:"
  echo "  -h, --help         Display this help message."
}

# TODO Retrieve the required arguments: user, password and roles

# TODO check if the required arguments are passed

# Verify that the script runs from the correct folder
./scripts/check_working_directory.sh --path "$ROOT_DIRECTORY"

# Check if Elasticsearch container is running
case $(docker inspect -f '{{.State.Running}}' "$ES_DOCKER_CONTAINER") in
  true)
    # Docker container is running
    echo "Docker container is already running."
    echo
    ;;
  false)
    # Docker container is NOT running
    echo "Docker container is not running."
    echo "Restarting Docker container."
    docker container start "$ES_DOCKER_CONTAINER"
    echo

    # Wait few seconds to let Elasticsearch start
    i=0
    while [ $i -lt 120 ]; do
        echo "Starting Elasticsearch..."
        i=$((i + 2))
        sleep 2
    done
    ;;
  *)
    # Docker container does not exist
    echo "Docker container does not exist. Please run the command: just setup_elasticsearch"
    echo
    ;;
esac

# TODO
# Check if Elasticsearch is reachable

# TODO
# Create Elasticsearch user