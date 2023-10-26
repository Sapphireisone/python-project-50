install:
		poetry install

lint:
		poetry run flake8 gendiff

check:
		poetry check

build:
		poetry build
