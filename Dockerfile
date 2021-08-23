FROM python:3.9-alpine
MAINTAINER Oleksandr Oliynyk

ENV PYTHONUNBUFFERED 1

COPY ./packages.txt /packages.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /packages.txt
RUN apk del .tmp-build-deps

RUN mkdir /api
WORKDIR /api
COPY ./api /api

RUN adduser -D oleksandr
USER oleksandr


