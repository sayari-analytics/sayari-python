# Check Python version (must be 3.9 or higher)
check-python-version:
	python -c "import sys; assert sys.version_info >= (3, 9), 'Python 3.9 or higher is required!'"

# Install runtime dependencies using pip
setup:
	pip install python-dotenv

# Install development dependencies and ensure types-python-dotenv is included
setup-poetry:
	curl -sSL https://install.python-poetry.org | python - -y --version 1.5.1
	poetry add --dev types-python-dotenv
	poetry install

# Run mypy type checks
run-poetry:
	poetry run mypy --ignore-missing-imports .

# Local installation using pip
local-install:
	pip install .

# Run tests with pytest
test:
	pytest -v

# Run PEP8 and Pylint lint checks
lint:
	poetry run pylint examples/*.py
	poetry run flake8 examples/*.py

# All-in-one command to run all checks
all-checks: check-python-version setup setup-poetry run-poetry lint test
