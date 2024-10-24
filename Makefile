# Setup deps
setup:
	pip install python-dotenv

setup-poetry:
	curl -sSL https://install.python-poetry.org | python - -y --version 1.5.1
	poetry add --dev types-python-dotenv
	poetry install

run-poetry:
	poetry run mypy .

local-install:
	pip install .

test:
	pytest -v
