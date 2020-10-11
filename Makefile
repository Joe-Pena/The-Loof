build:
	docker build --force-rm $(options) -t the_loof:latest .

start:
	docker-compose up --remove-orphans $(options)

stop:
	docker-compose down --remove-orphans $(options)

restart:
	docker-compose down --remove-orphans $(options)
	docker-compose up --remove-orphans $(options)

manage:
	docker-compose run $(options) the_loof python manage.py $(cmd)

migrate:
	docker-compose run $(options) the_loof python manage.py migrate

migrations:
	docker-compose run $(options) the_loof python manage.py makemigrations

populate-db:
	docker-compose run $(options) the_loof python manage.py loaddata ./setup/fixtures/db_backup.json

shell:
	docker-compose run $(options) the_loof python manage.py shell

bash:
	docker-compose run $(options) the_loof bash

initialize:
	docker build --force-rm $(options) -t the_loof:latest .
	docker-compose run $(options) the_loof python manage.py makemigrations
	docker-compose run $(options) the_loof python manage.py migrate
	docker-compose run $(options) the_loof python manage.py loaddata ./setup/fixtures/db_backup.json
	docker-compose up --remove-orphans $(options)