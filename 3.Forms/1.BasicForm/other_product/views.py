from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import OtherProductForm


def index(request):
    if request.method == "POST":
        form = OtherProductForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/completed")

    else:
        form = OtherProductForm()

    return render(request, "product/index.html", {"form": form})


def other_product_created_feedback(request):
    return render(request, "other_product/completed.html")
