class movie: 

    def __init__(self, movie_id, title, runtime, genre):
        self.movie_id = movie_id
        self.title = title
        self.runtime = runtime
        self.genre = genre 

    def __str__(self):
        return f"title: {self.title}   runtime: {self.runtime}"

movie = movie("")