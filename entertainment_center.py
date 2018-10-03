# You must install Requests module in order to run this code.
# Use 'pip install requests' or 'easy_install requests' in your command line.
import requests
import media
import fresh_tomatoes
import json

# 'The Movie Database' API constants.
# IMAGE_BASE_URL and POSTER_FILE_SIZE were retrieved using this link:
# https://developers.themoviedb.org/3/configuration/get-api-configuration
# Since these values do not change often, a specific method to retrieve the
# data was not implemented.
# Create an API key in The Movie Database's website and replace variable
# API_KEY's value below. your-api-key-here!!!
API_KEY = "fa71f4f6a5a629f8e49e3ed1bfe31a6e"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/"
POSTER_FILE_SIZE = "w500"


# Retrieves a list of trending movies in the past week from
# 'The Movie Database' website using its API and returns a JSON object
# containing the full list.
def getTrendingMovies():
    url = "https://api.themoviedb.org/3/trending/movie/week?api_key=" + API_KEY
    http_response = requests.get(url)
    return http_response.json()


# Receives a JSON movie object and returns an instance of Movie class.
def createMovie(movieObject):
    title = movieObject['title']
    movieId = movieObject['id']
    posterUrl = IMAGE_BASE_URL + POSTER_FILE_SIZE + movieObject['poster_path']
    trailerUrl = getTrailerUrl(movieId)
    movieInstance = media.Movie(title, posterUrl, trailerUrl)
    return movieInstance


# Returns a complete URL to a movie trailer on Youtube, based on the movie id
# retrieved from 'The Movie Database' API.
def getTrailerUrl(movieId):
    url = ("https://api.themoviedb.org/3/movie/{0}"
           "/videos?api_key={1}&language=en-US").format(str(movieId), API_KEY)
    http_response = requests.get(url)
    jsonObject = http_response.json()
    availableTrailers = jsonObject['results']
    if availableTrailers:
        return "https://www.youtube.com/watch?v=" + availableTrailers[0]['key']
    else:
        return ""


# Returns a list of Movie instances to be used by the
# fresh_tomatoes.open_movies_page method.
def createMovieList():
    movieList = []
    trendingMovies = getTrendingMovies()
    for result in trendingMovies['results']:
        newMovie = createMovie(result)
        movieList.append(newMovie)
    return movieList


# Main Code
print("Loading movies. Please wait...")
movies = createMovieList()
fresh_tomatoes.open_movies_page(movies)
