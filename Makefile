install:
		poetry install

lint:
		poetry run flake8 gendiff

test:
		pytest

build:
		poetry build
