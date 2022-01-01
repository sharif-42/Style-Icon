# Style-Icon

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/sharif-42/Style-Icon/graphs/commit-activity)
[![Maintainer](https://img.shields.io/badge/maintainer-Sharif_42-blue.svg)](https://github.com/sharif-42)
[![Generic badge](https://img.shields.io/badge/MadeWith-Python3.7-green.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/badge/FrameWork-Django3.2-%230db7ed.svg)](https://docs.djangoproject.com/en/3.2/)
[![Generic badge](https://img.shields.io/badge/FrameWork-DjangoRestFrameWork-red.svg)](https://www.django-rest-framework.org/)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![ElasticSearch](https://img.shields.io/badge/-ElasticSearch-005571?style=for-the-badge&logo=elasticsearch)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

Backend of Style-Icon. Style-Icon is an E-Commerce Site. Developed on Python3.7 and Django3.2. Here User can see various
products and product details. Can create cart and then order.

## Common commands for development in Docker

* Run Project in Docker
    ```shell
    docker-compose build
    docker-compose up
    ```
* Database Restore
  ```shell
  docker exec -it style-icon_db_1 psql -U style-icon -c "DROP SCHEMA public CASCADE;"
  docker exec -it style-icon_db_1 psql -U style-icon -c "CREATE SCHEMA public"
  cat <file_path> | docker exec -i style-icon_db_1 psql -U postgres
  ```  
* Run the test cases for unit test.
    ```shell
    docker-compose run django sh -c "python manage.py test"  
    ```
* To create and populate the Elasticsearch index and mapping use the search_index command:
  ```shell
  docker exec -it style-icon_django_1 sh -c "python manage.py search_index --rebuild -f"  # reindex
  docker exec -it style-icon_django_1 sh -c "python manage.py search_index --delete -f" # delete index
  docker exec -it style-icon_django_1 sh -c "python manage.py search_index --populate -f" # populate data 
   ```
* Necessary Management Commands
  ```shell
  # Create new app
  docker-compose run style-icon_django_1 sh -c "python manage.py startapp <App_Name>"
  # Migration commands
  docker exec -it style-icon_django_1 sh -c "python manage.py makemigrations"
  docker exec -it style-icon_django_1 sh -c "python manage.py migrate"
  # Create super user
  docker exec -it style-icon_django_1 sh -c "python manage.py createsuperuser"
  # Run shell
  docker exec -it style-icon_django_1 sh -c "python manage.py shell_plus"
  ```

## Run in Local Environment

* create a virtual environment to the root directory and then run the following commands.
  ```shell
  source venv/bin/activate  # venv is the virtual env name
  pip install -r requirements.txt
  python manage.py runserver
  ```