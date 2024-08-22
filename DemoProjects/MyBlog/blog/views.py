from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from .models import Post
from .forms import CommentForm


class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class PostsView(ListView):
    template_name = "blog/posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"


class PostView(View):
    def is_read_for_later_post(self, request, post_id):
        saved_posts = request.session.get("saved_posts")
        is_saved_for_later = False
        if saved_posts is not None:
            is_saved_for_later = post_id in saved_posts

        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "is_saved_for_later": self.is_read_for_later_post(request, post.id),
        }
        return render(request, "blog/post-details.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-page-name", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "is_saved_for_later": self.is_read_for_later_post(request, post.id),
        }
        return render(request, "blog/post-details.html", context)


class ReadLaterView(View):
    def get(self, request):
        saved_posts = request.session.get("saved_posts")

        context = {}

        if saved_posts is None or len(saved_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=saved_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/saved-posts.html", context)

    def post(self, request):
        saved_posts = request.session.get("saved_posts")

        if saved_posts is None:
            saved_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in saved_posts:
            saved_posts.append(post_id)
        else:
            saved_posts.remove(post_id)

        request.session["saved_posts"] = saved_posts

        return HttpResponseRedirect("/")
