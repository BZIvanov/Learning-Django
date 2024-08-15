from django.urls import path

# import everything from the views.py file
from . import views

urlpatterns = [
    path("", views.index, name="index-name"),
    path("algebra", views.algebra_view, name="algebra-name"),
    path("geometry", views.geometry_view, name="geometry-name"),
]
