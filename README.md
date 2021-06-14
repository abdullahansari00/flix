1. Setup database using postgresql according to the configurations given in settings file

2. Use following commands to import generes and movies respectively from the MovieDB APIs.
python manage.py import_generes
python manage.py import_movies

3. Go to /users/graphql/ to perform user queries and mutations like following:
	a. Registration
	b. Account verification
	c. Login
	d. Update account

	e. Me query
	f. User info using user ID
	g. All users list

4. Go to /geek/graphql/ to perform movies queries and mutations like following:
	a. View all movies
	b. View movie info using movie ID
	c. View watched movie list using list title
	d. View all your watched movies lists
	e. Get recommended movies list based on your watched movies list

	f. Create watched movies list using unique codename
	g. Add movies to watched movies list
	h. Remove movies from watched movies list
	i. Delete watched movies list

5. You need to be logged in to perform most of the functions. You can also use Authorization header and pass value "JWT {TOKEN FROM THE LOGIN}".

6. Refer to screenshots in "Screenshots" folder