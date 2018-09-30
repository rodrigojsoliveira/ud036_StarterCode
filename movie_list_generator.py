import movie
import fresh_tomatoes

a_bugs_life = movie.Movie("A Bug's Life",
                          "https://vignette.wikia.nocookie.net/pixar/images/c/ca/Bugs_life_ver5_xlg.jpg/revision/latest?cb=20110515135005",
                          "https://www.youtube.com/watch?v=vhGlMv3UCXA")

movies = [a_bugs_life]

fresh_tomatoes.open_movies_page(movies)
                          
