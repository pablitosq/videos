import os
from flask import Flask, render_template, request, redirect, url_for
import requests

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
    
    def get_title(self, title):
        if request.method == 'POST':
        
            if request.form['opcion'] == "pelicula" or request.form['opcion'] == "serie" and request.form['search'] == "":
                
                message = "No has introducido ningún dato en la búsqueda"
            
        if request.form['opcion'] == "pelicula" and request.form['search'] != "":
            
            _search = request.form['search']
            
            url = f"https://api.themoviedb.org/3/search/movie?query={_search}&include_adult=false&language=en-US&page=1"
            
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
            }
            
            response = requests.get(url, headers=headers)
            response = response.json()

        print("Movie.get_title")

        return self.title
    def get_id_movie(self):
        print("Movie.get_id_movie")

        return self.id_movie
