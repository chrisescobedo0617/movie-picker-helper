import os
import sys
import argparse
import requests
from dotenv import load_dotenv

load_dotenv()


def get_movies(url):
    """Function to get a a list of movies"""
    response = requests.get(url)
    json_response = response.json()
    for count, value in enumerate(json_response.get('results'), start=1):
        print('\033[1m' + str(count) + '.' + ' ' + value.get('title'))


def get_overview(url):
    """Function to get the overview of each movie"""
    response = requests.get(url)
    json_response = response.json()
    for count, value in enumerate(json_response.get('results'), start=1):
        print(  '\033[1m' + str(count) + '.' + ' ' + value.get('title'))
        print('\033[0m')
        print(value.get('overview'))
        print('\n')


def get_nowplaying():
    """Function to get a list movies currently playing"""
    np_url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={os.environ["API_KEY"]}&language=en-US&page=1'
    response = requests.get(np_url)
    json_rsponse = response.json()
    for value in json_rsponse.get('results'):
        print(value.get('title'))


def get_genre_int(user_genre):
    genres_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={os.environ["API_KEY"]}&language=en-US'
    response = requests.get(genres_url)
    genres = response.json().get('genres')
    for genre in genres:
        if genre.get('name').lower() == user_genre:
            return genre.get('id')
    return None


def get_actor_int(user_actor):
    actor_url = f'https://api.themoviedb.org/3/search/person?api_key={os.environ["API_KEY"]}&language=en-US&query={user_actor}&page=1&include_adult=false'
    response = requests.get(actor_url)
    actors = response.json().get('results')
    for actor in actors:
        if actor.get('name').lower() == user_actor:
            return actor.get('id')
    return None


def create_parser():
    """Create a command line parser object with some arguments."""
    parser = argparse.ArgumentParser(
        description="Helps find a movie to watch depending on what the user feels like watching.")
    parser.add_argument(
        '-g', '--genre', help='Genre user wants to watch')
    parser.add_argument(
        '-y', '--year', help='Release year of movies the user wants to watch')
    parser.add_argument(
        '-n', '--nowplaying', action='store_true', help='Movies that are currently playing'
    )
    parser.add_argument(
        '-o', '--overview', action='store_true', help='Provides and overview of what the movies are about'
    )
    parser.add_argument(
        '-a', '--actor', help='Get movies featuring an actor'
    )
    return parser


def main(args):
    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args()
    if not ns:
        parser.print_usage()
        sys.exit(1)
    
    genre = ns.genre
    year = ns.year
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={os.environ["API_KEY"]}&language=en-US&sort_by=popularity.desc&page=1'


    if ns.genre:
        genre_int = get_genre_int(genre.lower())
        if genre_int:
            genre_strip = f'&with_genres={genre_int}'
            url += genre_strip
        else:
            print(f'No such genre: {genre}')
            sys.exit(1)
    if ns.year:
        year_strip = f'&primary_release_year={year}'
        url += year_strip
    if ns.actor:
        actor_int = get_actor_int(ns.actor.lower())
        if actor_int:
            actor_strip = f'&with_people={actor_int}'
            url += actor_strip
        else:
            print(f'No such actor named: {ns.actor}')
            sys.exit(1)  

    if (ns.genre and not ns.overview) or (ns.year and not ns.overview) or (ns.actor and not ns.overview):
        get_movies(url)
    if (ns.genre and ns.overview) or (ns.year and ns.overview) or (ns.actor and ns.overview) or (ns.year and ns.overview and ns.genre and ns.actor):
        get_overview(url)


    if ns.nowplaying:
        get_nowplaying()



if __name__ == '__main__':
    main(sys.argv[1:])