install:
	make production-install

production-install:
	pip install --upgrade pip && pip install -r requirements.txt

build:
	cp requirements.txt ../../containers/django_rest
	tar -czf ../../containers/django_rest/app.tar.gz \
		--exclude=tests api hotels manage.py > /dev/null 2>&1
	docker image build -t django_rest ../../containers/django_rest

run-debug:
	make reset-db setup-db
	SECRET_KEY=development DEBUG=True python manage.py runserver

run:
	SECRET_KEY=development python manage.py runserver

test:
	make unit-test

unit-test:
	DJANGO_SETTINGS_MODULE=api.settings pytest --cov=hotels --cov-report term-missing

clean:
	find . \( \
		-name '__pycache__' -o \
		-name '.coverage' -o \
		-name '.mypy_cache' -o \
		-name '.pytest_cache' -o \
		-name '*.pyc' -o \
		-name '*.pyd' -o \
		-name '*.pyo' -o \
		-name 'coverage.xml' -o \
		-name 'db.sqlite3' -o \
		-name 'htmlcov' -o \
	\) -print | xargs rm -rfv

coverage-html:
	coverage html

create-superuser:
	DJANGO_SUPERUSER_USERNAME="admin" \
	DJANGO_SUPERUSER_PASSWORD="development" \
	DJANGO_SUPERUSER_EMAIL="admin@development.com" \
	python manage.py createsuperuser --noinput

migrate:
	python manage.py migrate hotels

setup-db:
	python manage.py migrate --run-syncdb
	sqlite3 db.sqlite3 < data/create_test_data.sql
	make migrate

reset-db:
	rm -f db.sqlite3
