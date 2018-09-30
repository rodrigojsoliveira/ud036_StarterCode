import movie
import fresh_tomatoes
import urllib.request
import json

# 'The Movie Database' API constants. IMAGE_BASE_URL and POSTER_FILE_SIZE
# were retrieved using this link:
# https://developers.themoviedb.org/3/configuration/get-api-configuration
# Since these values do not change often, a specific method to retrieve the
# data was not implemented.
API_KEY = "fa71f4f6a5a629f8e49e3ed1bfe31a6e"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/"
POSTER_FILE_SIZE = "w500"


# Retrieves a list of trending movies in the past week from
# 'The Movie Database' website using its API and returns a JSON object
# containing the full list.
def getTrendingMovies():

    url = "https://api.themoviedb.org/3/trending/movie/week?api_key=" + API_KEY
    http_response = urllib.request.urlopen(url,None)
    jsonObject = json.load(http_response)
    return jsonObject


# Creates an instance of class Movie from a JSON object.
def createMovie(movieObject):
    title = movieObject['title']   
    poster = IMAGE_BASE_URL + POSTER_FILE_SIZE + movieObject['poster_path']
    trailer = ""
    movieInstance = movie.Movie(title, poster, trailer)
    return movieInstance


# Returns a list of Movie object to be used by the
# fresh_tomatoes.open_movies_page method.
def createMovieList():
    movieList = []
    trendingMovies = getTrendingMovies()
    for result in trendingMovies['results']:
        newMovie = createMovie(result)
        movieList.append(newMovie)
    return movieList


# Main Code    
movies = createMovieList()
fresh_tomatoes.open_movies_page(movies)
