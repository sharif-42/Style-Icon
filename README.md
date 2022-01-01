# Style-Icon

Backend of Style-Icon

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/sharif-42/Style-Icon/graphs/commit-activity)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![ElasticSearch](https://img.shields.io/badge/-ElasticSearch-005571?style=for-the-badge&logo=elasticsearch)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

## Up and Run the project

## Common commands for development in Docker

* Running Project
    ```shell
      docker-compose build
      docker-compose up
    ```
* To create an **superuser account**, use this command.
    ```shell
      docker-compose run django sh -c "python manage.py createsuperuser"
     ```
* Run the test cases for unit test.
    ```shell
      docker-compose run django sh -c "python manage.py test"  
    ```
* To create and populate the Elasticsearch index and mapping use the search_index command:
  ```shell
      docker-compose run django sh -c "python manage.py search_index --rebuild"  
    ```