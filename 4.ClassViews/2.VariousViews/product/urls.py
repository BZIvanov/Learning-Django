from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductView.as_view()),
    path("created", views.ProductCreatedView.as_view()),
    path("products", views.ProductListView.as_view()),
    path("products/<int:pk>", views.ProductDetailsView.as_view()),
]
