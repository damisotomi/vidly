from django.contrib import admin

# Register your models here.

from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('title', 'number_in_stock', 'daily_rate')
    # the comma is included so that python knows its a tuple


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
