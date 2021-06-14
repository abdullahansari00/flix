from django.core.management.base import BaseCommand
import requests
from geek.models import Movie, Genre


class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		for y in range(1,501):
			try:
				url = 'https://api.themoviedb.org/3/discover/movie?api_key=cc4b67c52acb514bdf4931f7cedfd12b&language=en-US&sort_by=popularity.desc&include_adult=true&include_video=false&page='+str(y)
				response = requests.get(url).json()
				movies = response['results']
				for movie in movies:
					if not Movie.objects.filter(movie_id = movie["id"]).exists():
						movie_obj = Movie.objects.create(
							adult = movie["adult"],
							movie_id = movie["id"],
							language = movie["original_language"],
							title = movie["title"],
							overview = movie["overview"],
							popularity = movie["popularity"],
							poster_path = f"https://image.tmdb.org/t/p/original{movie['poster_path']}",
							vote_average = movie["vote_average"],
							vote_count = movie["vote_count"]
						)
						try:
							movie_obj.release_date = movie["release_date"]
							movie_obj.save()
						except:
							pass
						genres = Genre.objects.filter(genre_id__in = movie["genre_ids"])
						movie_obj.genres.set(genres)
			except Exception as e:
				print(e)