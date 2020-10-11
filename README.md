# Hello, Fools!

This right here is my attempt at trying to impress you.

I'm not done yet, but will update this README when I am.

As the app is not deployed anywhere(yet) you can firstmost clone down this repo:

`gh repo clone Joe-Pena/The-Loof`

If you dont use the github CLI tool, simply clone down with either HTTPS or SSH, depending how you usually do it:

HTTPS:

`https://github.com/Joe-Pena/The-Loof.git`

SSH:

`git@github.com:Joe-Pena/The-Loof.git`

---

## Starting the app

To start the application, all you need to do is run this cool command:

`make initialize`

This will build the docker image, make and migrate migrations, populate the postgresql database, and finally, run the container. You only need to run this command the very first time you run the application.

If you have no access to the `make` command though, you will have to run the following:

```
docker build --force-rm $(options) -t the_loof:latest .
docker-compose run $(options) the_loof python manage.py makemigrations
docker-compose run $(options) the_loof python manage.py migrate
docker-compose run $(options) the_loof python manage.py loaddata ./setup/fixtures/db_backup.json
docker-compose up --remove-orphans $(options)
```

When you want to stop the application, simply run `make stop`, to start it again, run `make start`.

Finally there's a couple more commands you can use if you want to dive deeper into the app:

- `make build` - Builds the Docker image
- `make shell` - Starts a python shell from within the container.
- `make bash` - Starts a bash session inside the container.
- `make migrations` - CREATES migration files.
- `make migrate` - RUNS migrations.
- `make populate-db` - Populates the postgres db with the fixture found in `/setup/fixtures`, you shouldn't need to run this if you ran `make initialize` above.
