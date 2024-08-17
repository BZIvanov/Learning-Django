from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index-page-name"),
    path("<slug:slug>", views.movie, name="movie-page-name"),
]
