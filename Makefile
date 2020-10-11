build:
	docker build --force-rm $(options) -t the_loof:latest .

start:
	docker-compose up --remove-orphans $(options)

stop:
	docker-compose down --remove-orphans $(options)

manage:
	docker-compose run $(options) the_loof python manage.py $(cmd)

migrate:
	docker-compose run $(options) the_loof python manage.py migrate

migrations:
	docker-compose run $(options) the_loof python manage.py makemigrations

populate-db:
	docker-compose run $(options) the_loof python manage.py loaddata ./setup/fixtures/articles_fixture.json

shell:
	docker-compose run $(options) the_loof python manage.py shell

bash:
	docker-compose run $(options) the_loof bash