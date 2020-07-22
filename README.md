# movie-picker-helper
A simple program to help pick what movies to watch.
## After cloning
After you clone the repo you need to navigate to [The Movie DB website](https://www.themoviedb.org/login) and create an account and also sign up to access their api.
### Usage
* The user uses the command line to possibly pass in things they want in the movies returned.
### Command line arguments
You can use arguements one, two, and three seperate or together. Arguement four must be alone.
1. Supplying '--genre' 'genre_user_wants' returns movies based on what genre is passed in.
2. Supplying '--year' 'year_integer' returns movies based on what year is passed in.
3. Supplying '--actor' 'actor name' returns movies based on what actor is passed in.


4. Supplying '--nowplaying' returns movies that are currently playing.

**Supplying '--overview' alongside '--genre', 'year', or 'actor' or 'genre', 'year', and 'actor together returns an overview of what the movies are about**
