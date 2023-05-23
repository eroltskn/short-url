

<a name="docker"></a>
## Install (Run) with Docker

### About the Builds and Images in use:
We are using currently 2 services: the api (Django App), the db (the postgrSQL database).
    - __api:__ The Django Dockerfile is in the root directory, and it has an entrypoint file that connects the backend to the database and runs migrations.
    - __db:__ This is built and created from the postgres:13-alpine image. The default environment variables are set in the docker-compose.yml file.

### Runing Docker-Compose

1. Clone the repo:
    ```bash
    git clone https://github.com/eroltskn/short-url.git
    ```
   1. Configure the environment variables.
       1. The new .env.dev file should contain all the environment variables necessary to run all the django app in all the environments. However, the only needed variables for docker to run are the following:
           ```bash
           DEBUG=1
           SECRET_KEY=foo
           DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
           SQL_ENGINE=django.db.backends.postgresql
           SQL_DATABASE=hello_django_dev
           SQL_USER=hello_django
           SQL_PASSWORD=hello_django
           SQL_HOST=db
           SQL_PORT=5432
           ```
1. Run docker-compose:
    ```bash
    docker-compose up --build
    ```
1. Congratulations =) !!! The App should be running in [localhost:8000](http://localhost:8000)
1. (Optional step) To create a super user run:
    ```bash
    docker-compose run api ./manage.py createsuperuser
    ```
1. For testing endpoints :
    ```bash
    docker-compose exec web python manage.py test
    ```

1. Creating short url from client side  :
    ```bash
    curl --location 'http://localhost:8000/short_url/' \
    --header 'Content-Type: application/json' \
    --data '{
        "original_url":"https://www.youtube.com/taskin3"
    }'
    ```
1. Getting short url from client side  :
    ```bash
      curl --location 'http://localhost:8000/short_url/?converted_url=xzq7jik3'
    ```


