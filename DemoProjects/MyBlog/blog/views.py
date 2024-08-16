from django.shortcuts import render
from datetime import date

dummy_posts = [
    {
        "slug": "hiking",
        "image": "mountains.png",
        "author": "Biser",
        "date": date(2024, 8, 21),
        "title": "Hiking",
        "excerpt": "Hiking is fun",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """,
    },
    {
        "slug": "programming",
        "image": "mountains.png",
        "author": "Biser",
        "date": date(2024, 3, 10),
        "title": "Programming",
        "excerpt": "Programming is fun",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """,
    },
]


def get_date(post):
    return post["date"]


def index(request):
    sorted_posts = sorted(dummy_posts, key=get_date)
    latest_posts = sorted_posts[-2:]

    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/posts.html", {"posts": dummy_posts})


def post(request, slug):
    selected_post = next(post for post in dummy_posts if post["slug"] == slug)

    return render(request, "blog/post-details.html", {"post": selected_post})
