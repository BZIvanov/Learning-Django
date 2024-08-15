from django.urls import path

from . import views

urlpatterns = [
    path("mountains", views.nature_view, name="mountains-name"),
]
