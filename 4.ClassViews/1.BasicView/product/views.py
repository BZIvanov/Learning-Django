from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from .forms import ProductForm


class ProductView(View):
    def get(self, request):
        form = ProductForm()

        return render(request, "product/index.html", {"form": form})

    def post(self, request):
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/completed")

        return render(request, "product/index.html", {"form": form})


def product_created_feedback(request):
    return render(request, "product/completed.html")
