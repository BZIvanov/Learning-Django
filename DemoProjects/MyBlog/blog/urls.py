from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index-page-name"),
    path("posts", views.PostsView.as_view(), name="posts-page-name"),
    path("posts/<slug:slug>", views.PostView.as_view(), name="post-page-name"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later-name"),
]
