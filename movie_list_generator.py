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


# Receives a JSON movie object and returns an instance of Movie class.
def createMovie(movieObject):
    title = movieObject['title']
    movieId = movieObject['id']
    posterUrl = IMAGE_BASE_URL + POSTER_FILE_SIZE + movieObject['poster_path']
    trailerUrl = getTrailerUrl(movieId)
    movieInstance = movie.Movie(title, posterUrl, trailerUrl)
    return movieInstance


# Returns a complete URL to a movie trailer on Youtube, based on the movie id
# retrieved from 'The Movie Database' API.
def getTrailerUrl(movieId):
    url = "https://api.themoviedb.org/3/movie/" + str(movieId) + "/videos?api_key=" + API_KEY + "&language=en-US"
    http_response = urllib.request.urlopen(url,None)
    jsonObject = json.load(http_response)
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
movies = createMovieList()
print(len(movies))
fresh_tomatoes.open_movies_page(movies)
