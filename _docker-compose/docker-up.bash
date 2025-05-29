docker-compose rm -f
COMPOSE_HTTP_TIMEOUT=200 docker compose up --build --force-recreate --remove-orphans > docker.log
