import requests
from genres import movie_genres
import sys
import argparse


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
    np_url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=54bb31247dabf5791bce265c2fa2cd4f&language=en-US&page=1'
    response = requests.get(np_url)
    json_rsponse = response.json()
    print(np_url)
    for value in json_rsponse.get('results'):
        print(value.get('title'))


def genre_to_int(genre):
    inetger = movie_genres.get(genre)
    return inetger


def create_parser():
    """Create a command line parser object with some arguments."""
    parser = argparse.ArgumentParser(
        description="Helps find a movie to watch depending on what the user feels like watching.")
    parser.add_argument(
        '-g', '--genre', help='Genre user wants to watch')
    parser.add_argument(
        '-y', '--year', help='Release year of movies the user wants to watch')
    parser.add_argument(
        '-np', '--nowplaying', action='store_true', help='Movies that are currently playing'
    )
    parser.add_argument(
        '-ov', '--overview', action='store_true', help='Provides and overview of what the movies are about'
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
    url = f'https://api.themoviedb.org/3/discover/movie?api_key=54bb31247dabf5791bce265c2fa2cd4f&language=en-US&sort_by=popularity.desc&page=1'


    if ns.genre:
        genre.lower()
        g_int = genre_to_int(genre)
        genre_strip = f'&with_genres={g_int}'
        url += genre_strip
    if ns.year:
        year_strip = f'&primary_release_year={year}'
        url += year_strip

    if ns.genre and not ns.overview or ns.year and not ns.overview:
        get_movies(url)
    if ns.genre and ns.overview or ns.year and ns.overview or ns.year and ns.overview and ns.genre:
        get_overview(url)


    if ns.nowplaying:
        get_nowplaying()


if __name__ == '__main__':
    main(sys.argv[1:])