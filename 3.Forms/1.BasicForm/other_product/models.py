from django.db import models


class OtherProduct(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
