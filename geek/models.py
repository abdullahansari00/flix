from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
	genre_id = models.IntegerField()
	genre_name = models.CharField(max_length = 100)

	def __str__(self):
		return(self.genre_name)


class Movie(models.Model):
	adult = models.BooleanField(default = False, null = True)
	genres = models.ManyToManyField(Genre, blank = True)
	movie_id = models.IntegerField(null = True)
	language = models.CharField(max_length = 20, null = True)
	title = models.CharField(max_length = 300, null = True)
	overview = models.TextField(null = True)
	popularity = models.FloatField(null = True)
	poster_path = models.TextField(null = True)
	release_date = models.DateField(null = True)
	vote_average = models.FloatField(null = True)
	vote_count = models.IntegerField(null = True)

	def __str__(self):
		return(self.title)


class WatchedMovies(models.Model):
	title = models.CharField(max_length = 100, null = True)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	movies = models.ManyToManyField(Movie, blank = True)

	def __str__(self):
		return(f"{self.user.username} - {self.title}")