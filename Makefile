# Setup deps
setup:
	pip install -r ./src/sayari/requirements.txt

setup-poetry:
	curl -sSL https://install.python-poetry.org | python - -y --version 1.5.1
	poetry install

run-poetry:
	poetry run mypy .

local-install:
	pip install .

test:
	pytest -v
