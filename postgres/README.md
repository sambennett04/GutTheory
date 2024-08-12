# Postgresql

Postgres is a relational database. Other relational databases are SQL Server, MySQL, Oracle Database, etc...
Relational databases are critical devices used to read, write, update, and delete an application's data.
Postgres is generally considered the best database for read and write workloads although MySQL can be more performant than postgres for read-only workloads. Read more about Postgres on the [project's official site](https://www.postgresql.org/). 

*Credits*
1. [Awesome Compose Examples](https://github.com/docker/awesome-compose/tree/master/postgresql-pgadmin) - great place to start
2. [Medium Article](https://medium.com/@jewelski/quickly-set-up-a-local-postgres-database-using-docker-5098052a4726) - ok material


## Postgres Docker Build & Run

1. Build the container

```sh

docker build -t guttheory-postgres

```

2. Create a file named .env from the ```.template.env``` file. Remeber to fill in the values.

```env

POSTGRES_USER=[your user]
POSTGRES_PW=[your password]
POSTGRES_DB=postgres

```

3. Run the container (environment variables sourced from .env, recommended)

```sh

docker run --name guttheory-postgres-container -d -p 5432:5432 --env-file ".env" guttheory-postgres 

```

4. Run the container (manually specify env vars, not recommended)

```sh

docker run --name guttheory-postgres-container -p 5432:5432 \
-e "POSTGRES_USER=[your pg user name]" \
-e "POSTGRES_PASSWORD=[your pg password]" \
-e "POSTGRES_DB=postgres" \
guttheory-postgres

```

**Use host.docker.internal as value for host name/address in pgdamin when connecting to database**

## Run Postgres and PG Admin

1. Copy the file ```.template.env``` to a new file named ```.env```
2. The ```.env``` file specifies a few different properties that are required to run the pg database and pg admin:

| Env Var Name | Description | Sample Value |
| -- | -- | -- |
| POSTGRES_USER | user name to log into pg database | phil |
| POSTGRES_PW | password to log into pg database | hotSoup1 |
| POSTGRES_DB | the name of the initial database in your postgres deployment | postgres |
| PGADMIN_MAIL | any email, user name to log into pg admin | phil@phil.com |
| PGADMIN_PW | password to log into pg admin ui | coldSoup2 |

3. Fill in the values you want to use for each item in your ```.env``` file. **NEVER CHECK .env FILES INTO GIT. EVER.** These files store passwords and when passwords are uploaded to your public git repo you  get #hacked and the security of your service is compromised.

4. Navigate to the folder ```GutTheory/postgres```

```sh

cd GutTheory/postgres

```

5. Start the containers for pg database and pg admin with the following command:

```sh

# this command creates two containers 
# 1. postgres: this is the database service
# 2. pgadmin: this is the pg admin sql ide/management app
docker compose up

```

6. Connect to pgadmin the service by navigating to ```localhost:5050``` in your browser. Login with the values for ```PGADMIN_MAIL``` and ```PGADMIN_PW``` that you provided in the ```.env``` file.

![pgadmin screenshot](../images/Screenshot%202024-07-19%20at%2010.41.31 PM.png)

7. Once you are logged into pgadmin right click on ```servers``` in the top left-hand corner of the screen then click through to ```register``` > ```server```. Then fill in the following information when registering the server:

![pgadmin screenshot 1](../images/Screenshot%202024-07-19%20at%2010.46.16 PM.png)
![pgadmin screenshot 2](../images/Screenshot%202024-07-19%20at%2010.46.56 PM.png)

8. You should now see your connection on the left-hand side of the screen under the server group you chose in step 7.

9. Open the query tool and run the following SQL commands:

```sql

-- should return 0
SELECT * FROM dbo.user

```

```sql

-- should show the schema of the table but no rows 
-- becaue the table is empty
SELECT COUNT(1) FROM dbo.user

```

The schema ```dbo``` and the table ```user``` under that schema were created by the file ```init.sql```. The ```init.sql``` file was mounted (copied) to the docker image for prostgres database to a specific location where postgres will try to execute any sql files found in that location. See line 12 of ```compose.yml``` for more details.

10. Stop the containers:

```sh

docker compose down

```

11. Stop the containers and remove all associated files:

```sh

docker compose down -v

```