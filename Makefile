# Setup deps
setup:
	pip install -r ./sdk/requirements.txt

# Push to GCP registry
gcp-build-push:
	python3 -m build
	python3 -m twine upload --repository-url https://us-east1-python.pkg.dev/sayari-datastore/sayari-python/ dist/* --verbose

install:
	pip install --upgrade sayari-python --extra-index-url https://us-east1-python.pkg.dev/sayari-datastore/sayari-python/simple/

test:
	cd tests; pytest -v
