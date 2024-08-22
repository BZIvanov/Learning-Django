# MyBlog Project

## Running the project

Run the following two commands to generate the migrations and the SQLite database file:

```
python manage.py makemigrations
python manage.py migrate
```

Create admin user with the following command:

```
python manage.py createsuperuser
```

Start the server with the following command:
```
python manage.py runserver
```

and visit `http://localhost:8000/admin/` to create some data and visit `http://localhost:8000/` for our blog site.


## Install additional dependencies

Install `Pillow` package, which is used for uploading files.

```
python -m pip install Pillow
```
