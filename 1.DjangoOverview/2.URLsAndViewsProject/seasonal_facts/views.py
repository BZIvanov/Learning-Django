from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


def seasonal_facts(request, season):
    sf = "Any season is your favourite season"

    if season == "winter":
        sf = "You favourite season is cold"
    elif season == "summer":
        sf = "You favourite season is hot"
    elif season == "autumn" or season == "spring":
        sf = "You favourite season is normal"

    return HttpResponse(sf)


def seasonal_facts_numbered(request, season):
    sf = None

    if season == 1:
        sf = "winter"
    elif season == 2:
        sf = "spring"
    elif season == 3:
        sf = "summer"
    elif season == 4:
        sf = "autumn"
    else:
        return HttpResponseNotFound("Invalid season number")

    # season-name matches the name in urlpatterns list
    # we will construct the redirect url to "/seasonal-facts/summer" for example
    redirect_path = reverse("season-name", args=[sf])

    return HttpResponseRedirect(redirect_path)
