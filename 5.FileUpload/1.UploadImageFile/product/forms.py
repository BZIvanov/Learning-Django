from django import forms


class ProductForm(forms.Form):
    product_image = forms.FileField()
