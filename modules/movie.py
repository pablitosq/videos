import os

class Movie():
    def __init__(self, id_movie, title, poster_path, overview, release_date, vote_average, vote_count):
        self.id_movie = id_movie
        self.title = title
        self.poster_path = poster_path
        self.poster = poster_path
        self.overview = overview
        self.release_date = release_date
        self.vote_average = vote_average
        self.vote_count = vote_count
    
    def get_id_movie(self):
        print("Movie.get_id_movie")

        return self.id_movie