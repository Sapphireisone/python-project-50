install:
	poetry install

lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest

build:
	poetry build

test-coverage:
	poetry run pytest --cov=gendiff

.PHONY: install lint pytest build
