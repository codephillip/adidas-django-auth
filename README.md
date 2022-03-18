# adidas_django_auth app

### Run the app in terminal

1. Start a Postgres database server on your machine or in the cloud.
2. Set the following environment variables in your terminal.

```
export POSTGRES_HOST=<address-where-database-running>
export POSTGRES_PORT=<port-where-database-running>
export POSTGRES_DB=<database-name>
export POSTGRES_USER=<username-for-database>
export POSTGRES_PASSWORD=<password-to-database>
```

3. Install packages and start the application server.

```
$ make install
$ make migrate
$ make run
```

### Run the app inside a Docker container

1. Build the docker container and get it up and running.

```
$ docker-compose build
$ docker-compose up
```

2. Setup database tables by running migrations.

```
$ docker-compose exec web python manage.py makemigrations
$ docker-compose exec web python manage.py migrate
```

### Make API calls against the server

1. Go to [http://localhost:8000/swagger](http://localhost:8000/swagger) to see Swagger documentation for API endpoints.
2. Run the APIs by clicking the "Try it now" button on the Swagger page.

### Run Django admin dashboard

1. Setup a password to login to the Django admin dashboard.

```
make adminuser password=<choose-a-secure-password>
```

2. Go to [http://localhost:8000/admin](http://localhost:8000/admin) and login to the dashboard using username `admin` and the password you chose in step 1 above.

### Run tests and check code coverage

```
$ make test
$ make coverage
```

### Lint your code

```
$ make lint
```
