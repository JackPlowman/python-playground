development-install:
	pip install --upgrade pip && pip install -r applications/requirements-dev.txt

python-lint:
	ruff check applications --fix

python-lint-check:
	ruff check applications

python-format:
	ruff format applications

python-format-check:
	ruff format --check applications

python-pre-commit:
	make python-lint python-format

coverage-combine-and-report:
	coverage combine django_rest-coverage/.coverage
	coverage xml
