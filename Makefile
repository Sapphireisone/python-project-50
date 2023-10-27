install:
		poetry install

lint:
		poetry run flake8 gendiff

pytest:
		poetry run pytest

build:
		poetry build
