from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index-page-name"),
    path("completed", views.product_created_feedback, name="completed-page-name"),
]
