from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from .forms import ProductForm
from .models import Product


class CreateProductView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, "product/index.html", {"form": form})

    def post(self, request):
        submitted_form = ProductForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            product = Product(image=request.FILES["product_image"])
            product.save()
            return HttpResponseRedirect("/")

        return render(request, "product/index.html", {"form": submitted_form})


class ProductsView(ListView):
    model = Product
    template_name = "product/products.html"
    context_object_name = "products"
