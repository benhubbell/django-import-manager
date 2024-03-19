# -- BASE --
FROM python:3.12 as base

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y netcat-traditional

RUN pip install --upgrade pip

# -- DEV --
FROM base as dev
COPY requirements/common.txt requirements/common.txt
COPY requirements/dev.txt requirements/dev.txt
RUN pip install -r requirements/dev.txt

COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

COPY . /app
ENV APP_ENV=dev
ENTRYPOINT ["/app/entrypoint.sh"]

# -- DEV --
FROM base as prod
COPY requirements/common.txt requirements/common.txt
COPY requirements/prod.txt requirements/prod.txt
RUN pip install -r requirements/prod.txt

COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

COPY ./src/django_import_manager /app
RUN mkdir /app/staticfiles
ENV APP_ENV=prod
ENTRYPOINT ["/app/entrypoint.sh"]

# -- BUILDER --
# FROM python:3.12 as builder

# WORKDIR /usr/src/app

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# RUN apt-get update
# RUN apt-get install -y --no-install-recommends gcc

# COPY requirements/common.txt requirements/common.txt
# COPY requirements/prod.txt requirements/prod.txt
# RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements/prod.txt

# # -- PROD --
# FROM python:3.11.4-slim-buster as prod

# RUN addgroup --system app
# RUN adduser --system --group app

# ENV APP_HOME=/app
# RUN mkdir $APP_HOME
# RUN mkdir $APP_HOME/staticfiles
# WORKDIR $APP_HOME

# RUN apt-get update
# RUN apt-get install -y --no-install-recommends netcat-traditional
# COPY --from=builder /usr/src/app/wheels /wheels
# COPY --from=builder /usr/src/app/requirements/prod.txt .
# RUN pip install --upgrade pip
# RUN pip install --no-cache /wheels/*

# COPY entrypoint.sh .
# RUN chmod +x $APP_HOME/entrypoint.sh

# COPY src/django_import_manager $APP_HOME

# RUN chown -R app:app $APP_HOME

# USER app

# ENTRYPOINT ["/app/entrypoint.sh"]
