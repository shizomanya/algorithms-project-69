install:
	poetry install

lint:
	poetry run flake8 search_engine

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=search_engine --cov-report=xml