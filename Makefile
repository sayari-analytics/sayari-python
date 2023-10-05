# Setup deps
setup:
	pip install -r ./src/sayari/requirements.txt

# Push to GCP registry
gcp-build-push:
	python3 -m build
	python3 -m twine upload --repository-url https://us-east1-python.pkg.dev/sayari-datastore/sayari-python/ dist/* --verbose
	rm -rf ./dist

install:
	pip install --upgrade sayari --extra-index-url https://us-east1-python.pkg.dev/sayari-datastore/sayari-python/simple/

test:
	cd src/sayariexit; pytest -v
