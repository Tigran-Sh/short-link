.DEFAULT_GOAL := build

run-docker-compose-command:
	docker compose ${command}
dc: run-docker-compose-command

build-image: command=build short-link
build-image: dc

manage-python:
	docker compose run --rm short-link $(command)

migrate: command=alembic upgrade head
migrate: manage-python

run: command=up short-link
run: dc

bash: command=run --rm short-link sh
bash: dc
