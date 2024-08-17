from django.contrib import admin

from .models import Movie


# with this class we will provide our custom configuration for the admin panel, otherwise default will be used
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("creator", "rating")


# this was we can add the Movie model to be administrated by the admin app
# it is not necessary all our models to be administrated by the admin panel
admin.site.register(Movie, MovieAdmin)
