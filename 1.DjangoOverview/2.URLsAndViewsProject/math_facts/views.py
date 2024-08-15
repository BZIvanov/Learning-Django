from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from math import pi


def index(request):
    algebra_redirect_path = reverse("algebra-name")
    geometry_redirect_path = reverse("geometry-name")

    response_data = f'<ul><li><a href="{algebra_redirect_path}">Algebra</a></li><li><a href="{geometry_redirect_path}">Geometry</a></li></ul>'

    return HttpResponse(response_data)


def algebra_view(request):
    return HttpResponse("2 + 3 = 5")


def geometry_view(request):
    response_data = f"<h1>{pi}</h1>"

    return HttpResponse(response_data)
