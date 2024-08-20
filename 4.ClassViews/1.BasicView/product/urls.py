from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductView.as_view()),
    path("completed", views.product_created_feedback),
]
