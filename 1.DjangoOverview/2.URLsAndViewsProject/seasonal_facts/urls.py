from django.urls import path

# import everything from the views.py file
from . import views

urlpatterns = [
    # the order of the paths specified matters, if we place the str path before the int, it will use the number as string
    path("<int:season>", views.seasonal_facts_numbered, name="season-name-numbered"),
    path("<str:season>", views.seasonal_facts, name="season-name"),
]
