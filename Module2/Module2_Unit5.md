In the last module we briefly explained the process to migrate data for the newly created models to a database. We started by running the below command in order to tell Django that models had been added to the app and it needed to create a database schema. 

```python
python manage.py makemigrations dog_shelters
```

With this example we have used it to add a new schema to the database, but it is also used when any changes or edits are made to the models. This command does not change the database permanently but can be thought of as a staging step. 

The next step is to then take the data that was staged and make the permanent changes to the database by using the below command.

```python
python manage.py migrate
```

By having these two steps Django has set up a type of version control by keeping track of each migration. If we wanted to see the list of migrations that had happened within the database we could also use the below command to return a history.

```python
python manage.py showmigrations -l
```

These data files live inside each app as a migrations directory and are designed to be a part of its codebase. With this type of design Django migrations will perform the same way on the same dataset to always provide consistent results. This means what you see when developing the project will carry over as the same in production.

## Reversing migrations

In some cases data is migrated as a mistake and Django has provided a way to reverse it. For example, say the data had been migrated and the resulting output looks like below.

```output
python manage.py migrate
Operations to perform:
  Apply all migrations: dog_shelters
Running migrations:
  Rendering model states... DONE
  Applying dog_shelters.0015_auto... OK
```

In order to reverse this migration **dog_shelters.0015** we would have to use the number of the previous migration **dog_shelters.0014**.

```bash
python manage.py migrate dog_shelters 0014
```

By entering the above command it would then reverse the migration performed for **dog_shelters.0015**. There is also a way to reverse all migrations that have been performed on an app. In order to reverse all migrations we would enter `zero` instead of the number of the migration.

```bash
python manage.py migrate dog_shelters zero
```

## Schema support

While Django supports all schema migrations that are shipped with its framework there are some that are better than others. Let's quickly examine the three most popular.

PostgreSQL | SQL | SQLite
-----------|-----|----------
Most competent in schema migrations, but if prior to PostgreSQL 11 recommended creating new columns with `null=True` in order to not cause a full rewrite of the table. | Lacks support for schema alteration operations, rewrites tables for almost every operation, and has small limits on name lengths for columns, tables and indexes. | Has very little built-in schema alteration support, can be slow and buggy, and not recommended to run in a production environment.