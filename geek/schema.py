from graphene_django.types import DjangoObjectType
import graphene
import requests
from .models import *


class MovieType(DjangoObjectType):
	class Meta:
		model = Movie
		fields = "__all__"


class WatchedMoviesType(DjangoObjectType):
	class Meta:
		model = WatchedMovies
		fields = "__all__"

# Query

class Query(graphene.ObjectType):
	all_movies = graphene.List(MovieType)
	def resolve_all_movies(root, info):
		return Movie.objects.all()


	movie = graphene.Field(MovieType, id = graphene.Int())
	def resolve_movie(root, info, id):
		return Movie.objects.get(id = id)


	watched_movies_list = graphene.List(MovieType, title = graphene.String())
	def resolve_watched_movies_list(root, info, title):
		if not WatchedMovies.objects.filter(title = title, user = info.context.user).exists():
			raise Exception("Watched List with this name does not exists")

		watched_movies_obj = WatchedMovies.objects.get(title = title, user = info.context.user)
		return watched_movies_obj.movies.all()


	watched_movies_lists = graphene.List(WatchedMoviesType)
	def resolve_watched_movies_lists(root, info):
		return WatchedMovies.objects.filter(user = info.context.user)


	recommended_movies_list = graphene.List(MovieType, title = graphene.String())
	def resolve_recommended_movies_list(root, info, title):
		try:
			watched_movies_list = WatchedMovies.objects.get(user = info.context.user, title = title)
		except:
			raise Exception("Movie list with this ID does not exists for your account")

		watched_movies_ids = ",".join(map(str,[x for x in watched_movies_list.movies.all().values_list("movie_id", flat=True)]))
		recommended_movies_ids = []

		for x in range(1,3):
			url = 'https://api.themoviedb.org/3/movie/'+watched_movies_ids+'/recommendations?api_key=cc4b67c52acb514bdf4931f7cedfd12b&language=en-US&page='+str(x)
			response = requests.get(url).json()['results']
			for x in response:
				recommended_movies_ids.append(x['id'])

		return(Movie.objects.filter(movie_id__in = recommended_movies_ids))


# Inputs

class MovieInput(graphene.InputObjectType):
	id = graphene.Int()

class WatchedListInput(graphene.InputObjectType):
	title = graphene.String()
	movies = graphene.List(MovieInput)

# Mutation

class CreateWatchedMoviesMutation(graphene.Mutation):
	class Arguments:
		input = WatchedListInput(required = True)

	watched_movies = graphene.Field(WatchedMoviesType)

	def mutate(root, info, input = None):
		if WatchedMovies.objects.filter(title = input["title"], user = info.context.user).exists():
			raise Exception("Watched List with this name already exists")
		watched_movies_obj = WatchedMovies(title = input["title"])
		watched_movies_obj.user = info.context.user
		watched_movies_obj.save()

		for movie in input["movies"]:
			watched_movies_obj.movies.add(Movie.objects.get(**movie))

		return CreateWatchedMoviesMutation(watched_movies = watched_movies_obj)


class AddToWatchedList(graphene.Mutation):
	class Arguments:
		input = WatchedListInput(required = True)

	watched_movies = graphene.Field(WatchedMoviesType)

	def mutate(root, info, input = None):
		if not WatchedMovies.objects.filter(title = input["title"], user = info.context.user).exists():
			raise Exception("Watched List with this name does not exists")

		watched_movies_obj = WatchedMovies.objects.get(title = input["title"], user = info.context.user)
		for movie in input["movies"]:
			watched_movies_obj.movies.add(Movie.objects.get(**movie))

		return AddToWatchedList(watched_movies = watched_movies_obj)


class RemoveFromWatchedList(graphene.Mutation):
	class Arguments:
		input = WatchedListInput(required = True)

	watched_movies = graphene.Field(WatchedMoviesType)

	def mutate(root, info, input = None):
		if not WatchedMovies.objects.filter(title = input["title"], user = info.context.user).exists():
			raise Exception("Watched List with this name does not exists")

		watched_movies_obj = WatchedMovies.objects.get(title = input["title"], user = info.context.user)
		for movie in input["movies"]:
			watched_movies_obj.movies.remove(Movie.objects.get(**movie))

		return RemoveFromWatchedList(watched_movies = watched_movies_obj)


class DeleteWatchedList(graphene.Mutation):
	class Arguments:
		title = graphene.String()

	message = graphene.String()

	def mutate(root, info, title):
		if not WatchedMovies.objects.filter(title = title, user = info.context.user).exists():
			raise Exception("Watched List with this name does not exists")

		watched_movies_obj = WatchedMovies.objects.get(title = title, user = info.context.user)
		watched_movies_obj.delete()
		return DeleteWatchedList(message = "List successfully deleted!")



class Mutation(graphene.ObjectType):
	create_watched_list = CreateWatchedMoviesMutation.Field()
	add_to_watched_list = AddToWatchedList.Field()
	remove_from_watchedList = RemoveFromWatchedList.Field()
	delete_watched_list = DeleteWatchedList.Field()


schema = graphene.Schema(query = Query, mutation = Mutation)