install:
	-command -v poetry || pip install poetry
	poetry install

lint:
	poetry run lint

test:
	poetry run scripts/bash/test.sh
