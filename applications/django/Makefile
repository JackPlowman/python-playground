install:
	make development-install production-install

development-install:
	pip install --upgrade pip && pip install -r ../requirements-dev.txt

production-install:
	pip install --upgrade pip && pip install -r requirements.txt

run:
	SECRET_KEY=development python manage.py runserver
