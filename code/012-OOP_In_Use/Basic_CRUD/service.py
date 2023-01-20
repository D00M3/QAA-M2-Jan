# Business logic, creating movie objects and putting and pulling data from our db 

from movie import movie

# conn, cursor and DB connection stuff 

# Service as a class
class service:

    def createMovie(self, movie_id, title, runtime, genre):
        movieObj = movie(movie_id, title, runtime, genre)
        return(movieObj)

service1 = service()

print(service1.createMovie(4, "StarShip Troopers 4", 70, "Sci_Fi, Action"))

# Service as a file

def createMovie(self, movie_id, title, runtime, genre):
    movieObj = movie(movie_id, title, runtime, genre)
    return(movieObj)

print(createMovie(4, "StarShip Troopers 4", 70, "Sci_Fi, Action"))