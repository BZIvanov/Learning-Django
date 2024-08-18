from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Address(models.Model):
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.city}, {self.street}, {self.postal_code}"

    # we are overriding the name, because in django admin it will be "Addresss"
    class Meta:
        verbose_name_plural = "Address"


class Creator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Movie(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    is_recent = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    creator = models.ForeignKey(
        Creator, on_delete=models.CASCADE, null=True, related_name="movies"
    )
    actors = models.ManyToManyField(Actor)

    # override get_absolute_url method to include the id
    def get_absolute_url(self):
        return reverse("movie-page-name", args=[self.slug])

    def __str__(self):
        return f"{self.title} ({self.rating})"
