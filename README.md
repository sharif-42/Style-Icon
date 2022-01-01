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