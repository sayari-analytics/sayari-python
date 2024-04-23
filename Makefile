setup-poetry:
	curl -sSL https://install.python-poetry.org | python - -y --version 1.5.1
	poetry install

poetry:
	poetry run mypy .
