from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ProductForm
from .models import Product


def index(request):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            product = Product(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                rating=form.cleaned_data["rating"],
            )
            product.save()

            return HttpResponseRedirect("/completed")

    else:
        form = ProductForm()

    return render(request, "product/index.html", {"form": form})


def product_created_feedback(request):
    return render(request, "product/completed.html")
