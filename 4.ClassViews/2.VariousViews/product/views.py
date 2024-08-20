from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from .forms import ProductForm
from .models import Product


class ProductView(FormView):
    form_class = ProductForm
    template_name = "product/index.html"
    success_url = "/created"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductCreatedView(TemplateView):
    template_name = "product/product-created.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "Enjoy"
        return context


class ProductListView(ListView):
    template_name = "product/product-list.html"
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        base_query = super().get_queryset()
        filtered_data = base_query.filter(rating__gt=2)
        return filtered_data


class ProductDetailsView(DetailView):
    template_name = "product/product-details.html"
    model = Product
