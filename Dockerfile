# pull official base image
FROM python:3.7-alpine

RUN mkdir /code
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
#RUN apk update \
#    && apk add zlib-dev jpeg-dev gcc musl-dev \
#    && apk add postgresql-dev gcc python3-dev musl-dev

# install psycopg2 dependencies
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/

RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

COPY . /code/

RUN adduser -D user
USER user