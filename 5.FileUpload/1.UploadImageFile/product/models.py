from django.db import models


class Product(models.Model):
    image = models.FileField(upload_to="images")
