from django.contrib import admin

# Register your models here.
from django.contrib import admin

from movies.models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'ranking']

admin.site.register(Movie,MovieAdmin)

