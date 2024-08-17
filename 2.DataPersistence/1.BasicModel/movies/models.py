from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Movie(models.Model):
    creator = models.CharField(null=True, max_length=100)
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    is_recent = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True)

    # override get_absolute_url method to include the id
    def get_absolute_url(self):
        return reverse("movie-page-name", args=[self.slug])

    # override save method to create a slug on save
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
