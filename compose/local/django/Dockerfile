# pull official base image
FROM python:3.7-alpine

RUN mkdir /code
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN apk update \
#  # psycopg2 dependencies
#  && apk add --virtual build-deps gcc python3-dev musl-dev \
#  && apk add --update --no-cache --virtual .tmp-build-deps \
#  && apk add postgresql-dev \
#  && apk add build-base \
#  # CFFI dependencies
#  && apk add libffi-dev py-cffi \
#  # Translations dependencies
#  && apk add gettext \
#  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
#  && apk add postgresql-client \

# install psycopg2 dependencies
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

# install dependencies
RUN pip install --upgrade pip

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./compose/local/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

RUN apk del .tmp-build-deps

COPY . /code/

RUN adduser -D user
USER user

ENTRYPOINT ["/entrypoint"]