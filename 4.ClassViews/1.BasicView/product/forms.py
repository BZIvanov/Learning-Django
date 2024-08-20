from django import forms

from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["title", "description", "rating"]
        labels = {"title": "Title", "description": "Description", "rating": "Rating"}
        error_messages = {
            "title": {"required": "Field is required", "max_length": "Too long title"},
            "description": {
                "required": "Field is required",
                "max_length": "Too long description",
            },
            "rating": {"required": "Field is required"},
        }
