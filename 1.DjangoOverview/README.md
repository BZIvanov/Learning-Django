# Django overview

## Prerequisites

To use Django you need to have Python installed. Check the repository `Learning-Python` for more info.

You should also install Django from [here](https://www.djangoproject.com/download/).

To verify the installed version you can run `python -m django --version`.

## IDE

### VSCode

VSCode is great IDE to work with Python.

#### Extensions

Here is a list of recommended extensions:

- **Python** from Microsoft
- **Pylance** from Microsoft
- **Black Formatter** from Microsoft - check the extension description to read how to enable the formatting for python files.
- **Django** from Baptiste Darthenay - useful, if working with html templates

You can disable js Prettier extension in case you have it.

## Starting a new project

To start a new project run `django-admin startproject mysite`.

## Run a project

Use the following command to run a server `python manage.py runserver`.

## App

More info [here](https://docs.djangoproject.com/en/5.1/intro/tutorial01/#creating-the-polls-app).

Apps are self-contained components of a project that encapsulate specific functionality. Each app can handle a distinct part of the project's logic, such as user authentication, blog posts, or a shopping cart.

A Django project can be composed of multiple apps, each responsible for a different feature. For example, a project might have separate apps for user accounts, product listings, and order processing. Apps are reusable and can be plugged into other projects.

Django projects are usually a collection of apps that work together to form a complete application.

### Create new app

To create a new app run the following command `python manage.py startapp polls`, where _polls_ is the name we want to use for our app.

## HTML Templates

File formatting matters and might result in errors, if our file is uisng for example `extends`, `block`, `endblock`, etc... tempate tags and is bad formatted.
