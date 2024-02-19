APPLICATIONS:=django_rest,django_graphql

development-install:
	pip install --upgrade pip && pip install -r applications/requirements-dev.txt

install:
	make development-install
	find . -name "requirements.txt" -exec pip install -r {} \;

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
	coverage combine django_rest_coverage/.coverage django_graphql_coverage/.coverage
	coverage xml
