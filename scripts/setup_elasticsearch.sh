#!/bin/sh
# Setup an Elasticsearch instance through a Docker container
# Reference guide: https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html

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
if docker -v > /dev/null 2>&1 ; then
  echo "Docker is installed. Version:"
  docker --version
  echo
else
  echo "Docker is not installed. Please install Docker before running this script."
  echo
  exit 1
fi

# Check if Docker is running
if docker info > /dev/null 2>&1; then
  echo "Docker is running correctly."
  echo
else
  echo "Docker is not running. Please run Docker before running this script."
  echo
  exit 1
fi

# Check if the Docker network exists
if docker network inspect "$ES_DOCKER_NETWORK" > /dev/null 2>&1; then
  echo "Docker network '$ES_DOCKER_NETWORK' already exists."
  echo
else
  # Create the Docker network
  echo "Creating Docker network '$ES_DOCKER_NETWORK'"
  docker network create "$ES_DOCKER_NETWORK"
  echo "Docker network '$ES_DOCKER_NETWORK' created."
  echo
fi

# Pull the Elasticsearch Docker image
echo "Pulling Elasticsearch Docker image '$ES_DOCKER_IMAGE'"
echo
docker pull docker.elastic.co/elasticsearch/"$ES_DOCKER_IMAGE"
echo
echo "Elasticsearch Docker image '$ES_DOCKER_NETWORK' pulled."
echo

# Check if the container already exists and it is running
case $(docker inspect -f '{{.State.Running}}' "$ES_DOCKER_CONTAINER") in
  true)
    # Docker container is running
    echo "Docker container is already running."
    ;;
  false)
    # Docker container is NOT running
    # TODO
    echo "Docker container is not running."
    echo "Restarting Docker container."
    docker container start "$ES_DOCKER_CONTAINER"
    ;;
  *)
    # Create Docker container
    #TODO
    echo "Docker container is not created."
    echo "Starting Elasticsearch."
    echo
    docker container run --name "$ES_DOCKER_CONTAINER" --net "$ES_DOCKER_NETWORK" -p 9200:9200 -it -m 1GB \
      -e "discovery.type=single-node" \
      -e "ES_JAVA_OPTS=-Xms512m -Xmx512m" \
      --ulimit memlock=-1:-1 \
      --ulimit nofile=65536:65536 \
      -d \
      docker.elastic.co/elasticsearch/"$ES_DOCKER_IMAGE"
    echo
    # Wait for the specific output in the logs
    # TODO: Wait until ES is started
    # NOTE: When launched in background, no password is generated
#    while ! docker logs "$ES_DOCKER_CONTAINER" 2>&1 | grep -q "Password"; do
#        echo "Elasticsearch is starting..."
#        sleep 1
#    done
    echo "Elasticsearch Started."
    echo
    ;;
esac

# TODO: Retrieve the elastic password

# TODO: Check if the container is now running, otherwise exit

# Extract the elastic user password
# TODO: Check if the container is now running, otherwise exit
#docker logs "$ES_DOCKER_CONTAINER" | grep -A 1 Password | tail -n 1
#echo