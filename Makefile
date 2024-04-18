# Setup deps
setup:
	pip install -r ./src/sayari/requirements.txt

local-install:
	pip install .

test:
	pytest -v
