# Models demo

This demo shows how to create and use a model and also basic usage of the admin panel

## Usage

Run the following commands for the migrations:

```
python manage.py makemigrations 
python manage.py migrate  
```

Create admin user

```
python manage.py createsuperuser
```


Start the server

```
python manage.py runserver
```


Visit the Admin panel to create end edit data: `http://localhost:8000/admin/`

## Database

As you can see in the `settings.py` file, for this demo we are using the default used by Django SQLite, 
which is a file-based database. The file `db.sqlite3` is gitignored so you will need to create new admin user and data for your own database demo usage.