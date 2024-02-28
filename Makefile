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

coverage-combine-and-report:
	coverage combine django_rest_coverage/.coverage django_graphql_coverage/.coverage flask_rest_coverage/.coverage
	coverage xml

# ----------------------------------------------------------------------------
# SQL Lint

sql-lint-check:
	sqlfluff lint applications

sql-lint-fix:
	sqlfluff fix applications

# ----------------------------------------------------------------------------

pre-commit:
	make python-lint-check python-format-check

# ----------------------------------------------------------------------------
# Docker Compose

start:
	docker-compose -f containers/docker-compose.yml up -d

stop:
	docker-compose -f containers/docker-compose.yml down
