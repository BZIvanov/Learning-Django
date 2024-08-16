from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index-page-name"),
    path("posts", views.posts, name="posts-page-name"),
    path("posts/<slug:slug>", views.post, name="post-page-name"),
]
