development-install:
	pip install --upgrade pip && pip install -r ../requirements-dev.txt

python-lint:
	ruff check applications --fix

python-lint-check:
	ruff check applications

python-format:
	ruff format applications

python-format-check:
	ruff format --check applications
