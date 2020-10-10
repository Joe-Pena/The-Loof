build:
	docker build --force-rm $(options) -t the_loof:latest .

start:
	docker-compose up --remove-orphans $(options)

stop:
	docker-compose down --remove-orphans $(options)

manage:
	docker-compose run -rm $(options) the_loof python manage.py $(cmd)

