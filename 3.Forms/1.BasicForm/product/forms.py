from django import forms


class ProductForm(forms.Form):
    title = forms.CharField(
        label="Title",
        max_length=100,
        error_messages={"required": "Field is required", "max_length": "Too long text"},
    )
    description = forms.CharField(
        label="Description", widget=forms.Textarea, max_length=200
    )
    rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)
