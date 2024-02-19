install:
	make production-install

production-install:
	pip install --upgrade pip && pip install -r requirements.txt

run-debug:
	make reset-db setup-db
	DEBUG=True python manage.py runserver

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

# ----------------------------------------------------------------------------
# Docker

build-docker:
	cp requirements.txt ../../containers/docker/django_rest
	tar -czf ../../containers/docker/django_rest/app.tar.gz \
		--exclude=tests api hotels manage.py > /dev/null 2>&1
	docker image build -t django_rest ../../containers/docker/django_rest

run-docker:
	docker run -p 8000:8000 --detach \
		-e DJANGO_SUPERUSER_USERNAME=admin \
		-e DJANGO_SUPERUSER_PASSWORD=sekret1 \
		-e DJANGO_SUPERUSER_EMAIL=admin@example.com \
		django_rest

# ----------------------------------------------------------------------------
# Podman

build-podman:
		cp requirements.txt ../../containers/podman/django_rest
	tar -czf ../../containers/podman/django_rest/app.tar.gz \
		--exclude=tests api hotels manage.py > /dev/null 2>&1
	podman build -t django_rest ../../containers/podman/django_rest

run-podman:
		podman run -p 8000:8000 --detach \
		-e DJANGO_SUPERUSER_USERNAME=admin \
		-e DJANGO_SUPERUSER_PASSWORD=sekret1 \
		-e DJANGO_SUPERUSER_EMAIL=admin@example.com \
		localhost/django_rest
