from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProductView.as_view()),
    path("products", views.ProductsView.as_view()),
]
