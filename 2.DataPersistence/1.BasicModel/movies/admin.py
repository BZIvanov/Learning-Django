from django.contrib import admin

from .models import Creator, Movie, Address, Actor


# with this class we will provide our custom configuration for the admin panel, otherwise default will be used
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = (
        "creator",
        "rating",
    )
    list_display = (
        "title",
        "creator",
    )


# this way we can add our models to be administrated by the admin app
# it is not necessary all our models to be administrated by the admin panel
admin.site.register(Creator)
admin.site.register(Address)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)
