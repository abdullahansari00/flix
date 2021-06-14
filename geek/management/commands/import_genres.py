from django.core.management.base import BaseCommand
import requests
from geek.models import Genre


class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		url = "https://api.themoviedb.org/3/genre/movie/list?api_key=cc4b67c52acb514bdf4931f7cedfd12b&language=en-US"
		response = requests.get(url).json()
		genres = response['genres']

		for genre in genres:
			try:
				if not Genre.objects.filter(genre_id = genre["id"]).exists():
					Genre(
						genre_id = genre["id"],
						genre_name = genre["name"]
					).save()
			except Exception as e:
				print(e)