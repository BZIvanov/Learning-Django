from django import forms

from .models import OtherProduct


class OtherProductForm(forms.ModelForm):
    class Meta:
        model = OtherProduct
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
