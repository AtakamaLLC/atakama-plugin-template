DELETE_ON_ERROR:

env:
	python -m virtualenv env

requirements:
	pip install -r requirements.txt

lint:
	python -m pylint plugin_template
	black plugin_template

test:
	PYTHONPATH=. pytest --cov plugin_template --cov-fail-under=100 -v tests

install-hooks:
	pre-commit install

apkg:
	rm -rf dist
	flit build
	atakama-pkg --pkg dist/plugin_template-1.0.0-py3-none-any.whl --key ../keys/key.pem --crt ../keys/cert.pem --self-signed

.PHONY: test requirements lint publish install-hooks
