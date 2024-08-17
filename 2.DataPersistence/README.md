# Data persistence

## Migrations

Generally we should not manually create or edit files in our app's migrations folders. Django's migration system is designed to automatically handle database schema changes based on your models.

## Commands

- `python manage.py makemigrations` - create new migration files based on the changes you've made to your models. Migrations are a way to propagate changes you make to your Django models (such as adding a field, changing a field type, or deleting a model) into your database schema. It prepares the changes to your models so they can be applied to the database with the next step, usually done with `python manage.py migrate`

- `python manage.py migrate` - apply the migrations to your database. This command takes the migration files created by `makemigrations` and executes them, modifying your database schema to match your current models. It actually applies changes to your database, ensuring it matches the structure defined in your Django models.

## Django Admin

Read [here](https://docs.djangoproject.com/en/5.1/intro/tutorial02/#creating-an-admin-user) how to create admin user.

### Register admin user

Run the following command the create admin user `python manage.py createsuperuser`.

### Admin endpoint

Visit the following endpoint to access the admin `http://localhost:8000/admin/` (don't forget the trailing slash /).
