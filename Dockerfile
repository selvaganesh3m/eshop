FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /web

ADD . /web

COPY ./requirements.txt /web/requirements.txt

RUN pip install -r requirements.txt

COPY . /web
