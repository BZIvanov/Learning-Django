from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    posts = Post.objects.all().order_by("-date")

    return render(request, "blog/posts.html", {"posts": posts})


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(
        request, "blog/post-details.html", {"post": post, "post_tags": post.tags.all()}
    )
