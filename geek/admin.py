from django.contrib import admin
from geek.models import *

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
	list_display = ('genre_id', 'genre_name')


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie)
admin.site.register(WatchedMovies)