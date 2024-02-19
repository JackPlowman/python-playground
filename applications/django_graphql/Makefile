install:
	make production-install

production-install:
	pip install --upgrade pip && pip install -r requirements.txt

build:
	cp requirements.txt ../../containers/django_graphql
	tar -czf ../../containers/django_graphql/app.tar.gz \
		--exclude=tests api blog manage.py > /dev/null 2>&1
	docker image build -t django_graphql ../../containers/django_graphql

run-debug:
	make reset-db setup-db
	DEBUG=True python manage.py runserver

run:
	docker run -p 8000:8000 --detach \
		-e DJANGO_SUPERUSER_USERNAME=admin \
		-e DJANGO_SUPERUSER_PASSWORD=sekret1 \
		-e DJANGO_SUPERUSER_EMAIL=admin@example.com \
		django_graphql

test:
	make unit-test

unit-test:
	DJANGO_SETTINGS_MODULE=api.settings pytest --cov=blog --cov-report term-missing

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
	python manage.py migrate blog

setup-db:
	python manage.py migrate --run-syncdb
	sqlite3 db.sqlite3 < data/create_test_data.sql
	make migrate

reset-db:
	rm -f db.sqlite3
