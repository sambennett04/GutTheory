FROM postgres:latest

#specify enviroment variables
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}

COPY ./data/plant_foods.csv /tmp/list_plantf.csv
COPY ./init.sql /docker-entrypoint-initdb.d/init.sql
