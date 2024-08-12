# PG Admin

PG (postgres) Admin is an ide-like database management user interface where you can create different database objects like tables, databases, etc, and manage those objects. PG Admin makes developing against relational databases easier. Read more about PG Admin on the [project's site](https://www.pgadmin.org/).

## Docker Build & Run

1. Build the docker file.

```sh

docker build -t guttheory-pgadmin .

```

2. Use the ```.template.env``` file to create an ```.env``` file.

```env

PGADMIN_DEFAULT_EMAIL=phil@phil.com
PGADMIN_DEFAULT_PASSWORD=phil

```

3. Run the container.

```sh

docker run --name guttheory-pgadmin-container -d -p 5050:80 --env-file .env guttheory-pgadmin

```

4. Connect to pgadmin

```

localhost:5050

```

**Use host.docker.internal as value for host name/address in pgdamin when connecting to database**