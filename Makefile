THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY: up build test dev
up:
	docker-compose -f docker-compose.yml up --build
build:
	docker-compose -f docker-compose.yml build --no-cache
test:
	docker-compose -f docker-compose.yml -f docker-compose-tests.yml up --build
dev:
	docker-compose -f docker-compose.yml -f Docker_compose/docker-compose-dev.yml up --build
