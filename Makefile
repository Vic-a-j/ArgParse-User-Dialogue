# Constants
DC := docker-compose
APP_NAME := server


# Commands
.PHONY: ps
ps:
	$(DC) ps


.PHONY: build
build:
	$(DC) build


.PHONY: build-clean
build-clean:
	$(DC) build --no-cache


.PHONY: exec
exec:
	$(DC) exec $(APP_NAME) bash


.PHONY: up
up:
	$(DC) up


.PHONY: down
down:
	$(DC) down