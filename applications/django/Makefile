install:
	make production-install

production-install:
	pip install --upgrade pip && pip install -r requirements.txt

run-debug:
	make reset-db setup-db
	SECRET_KEY=development DEBUG=True python manage.py runserver

run:
	SECRET_KEY=development python manage.py runserver

create-superuser:
	python manage.py createsuperuser

migrate:
	python manage.py migrate hotels

setup-db:
	python manage.py migrate --run-syncdb
	sqlite3 db.sqlite3 < data/create_test_data.sql
	make migrate

reset-db:
	rm -f db.sqlite3
