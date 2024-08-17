from django.shortcuts import get_object_or_404, render
from django.db.models import Avg

from .models import Movie


def index(request):
    movies = Movie.objects.all().order_by("title")
    total_count = movies.count()
    avg_rating = movies.aggregate(Avg("rating"))

    return render(
        request,
        "movies/index.html",
        {"movies": movies, "total_count": total_count, "avg_rating": avg_rating},
    )


def movie(request, slug):
    movie = get_object_or_404(Movie, slug=slug)

    return render(
        request,
        "movies/movie.html",
        {"title": movie.title, "creator": movie.creator, "rating": movie.rating},
    )
