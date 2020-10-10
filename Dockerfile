FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

RUN apt-get update && \
  apt-get install -y \
  bash \
  build-essential \
  gcc \
  libffi-dev \
  openssl \
  postgresql \
  libpq-dev


COPY requirements.txt ./
RUN pip install -r ./requirements.txt

COPY manage.py ./manage.py
COPY the_loof ./the_loof

EXPOSE 8000

