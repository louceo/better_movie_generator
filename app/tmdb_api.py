import os
from dotenv import load_dotenv
import requests
import random


load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.themoviedb.org/3/discover/movie"
POSTER_URL = "https://image.tmdb.org/t/p/w500"
SEEN_IDS = set()

def get_movie(genre_id=None, sort="vote_average.desc"):
    global seen_ids
    params = {
        'api_key': API_KEY,
        'sort_by': sort,
        'vote_count.gte': 5000, 
        'vote_average.gte': 6.5,
        'page': 1,
        'with_genres': genre_id or "",
    }

    total_pages = get_pages(params)
    params['page'] = random.randint(1, total_pages)
    response = requests.get(BASE_URL, params=params)
    movies = response.json().get('results', [])
    if not movies:
        return {'title': 'Nothing here...'}
    available = [mv for mv in movies if mv['id'] not in SEEN_IDS]
    if not available:
        SEEN_IDS.clear()
        available = movies

    movie = random.choice(available)
    SEEN_IDS.add(movie['id'])
    trailer_url = get_trailer(movie['id'])

    return {
        'title': movie['title'],
        'overview': movie['overview'],
        'release_date': movie['release_date'],
        'poster': f'{POSTER_URL}{movie['poster_path']}',
        'trailer': trailer_url,
    }

def get_pages(params):
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    total_pages = data.get('total_pages')
    return total_pages

def get_trailer(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos'
    params = {"api_key": API_KEY, "language": "en-US"}
    response = requests.get(url, params=params)
    videos = response.json().get('results', [])
    for vd in videos:
        if vd['type'] == 'Trailer' and vd['site'] == 'YouTube':
            return f'https://www.youtube.com/watch?v={vd['key']}'
    return None

def get_genres():
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    params = {"api_key": API_KEY, "language": "en-US"}
    response = requests.get(url, params=params)
    genres = response.json()['genres']
    return genres
