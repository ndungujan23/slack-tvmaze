import requests
from omdbapi.movie_search import GetMovie


class Api:

    def __init__(self):
        self.url = "https://api.tvmaze.com"
        self.movie_url = "https://www.omdbapi.com/"
        self.movie_api_key = "75be129d"

    def search_show(self, query):
        response = requests.get(f"{self.url}/search/shows?q={query}")
        if response.ok:
            return response.json()
        else:
            return None

    def search_movie(self, query):
        movie = GetMovie(self.movie_api_key)
        return [movie.get_movie(title=query, plot='full')]
