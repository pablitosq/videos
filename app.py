from urllib import response
from flask import Flask, request, render_template, jsonify, redirect, url_for
from os.path import basename
import requests
import os
import sqlite3
import ntpath
from werkzeug.utils import secure_filename

app = Flask(__name__)
connection = sqlite3.connect('database/myvideos.db')
cur = connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_movie int NOT NULL,
    title TEXT NOT NULL,
    overview TEXT NOT NULL,
    img TEXT NOT NULL ) """)


@app.route('/')
def index():
    return render_template('app/index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    
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
            
            return render_template('app/search.html', response=response)
        
        if request.form['opcion'] == "serie" and request.form['search'] == "":
            
            _search = request.form['search']
            
            url = f"https://api.themoviedb.org/3/search/tv?query={_search}&include_adult=false&language=en-US&page=1"
            
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
            }

            response = requests.get(url, headers=headers)

            response = response.json()
            
            return render_template('movie/add-movie.html', response=response)
            
    return render_template('app/index.html', message=message,)

@app.route('/add-movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        
        if request.form['search'] == "":
            
            message = "No has introducido ningún dato en la búsqueda"
            return render_template('movies/add-movie.html', message=message)
            
        if request.form['search'] != "":
            
            _search = request.form['search']
            
            url = f"https://api.themoviedb.org/3/search/movie?query={_search}&include_adult=false&language=es-ES&page=1"
            
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
            }
            
            response = requests.get(url, headers=headers)
            response = response.json()
            
            print(response)
            
            return render_template('movies/add-movie.html', _search=_search ,response=response)
            
    return render_template('movies/add-movie.html')

@app.route('/add-movie-select', methods=['GET', 'POST'])
def add_movie_select():
    if request.method == 'POST':
        
        if request.form['id']:
            
            id = request.form['id']
            #print(movie_id)
            
            url = f"https://api.themoviedb.org/3/movie/{id}?language=es-ES"
            
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
            }
            
            response_movie = requests.get(url, headers=headers)
            response_movie = response_movie.json()
            
            print(response_movie)

            for genres in response_movie['genres']:
                print(genres['name'])
            
            #Créditos
                
            url2 = f"https://api.themoviedb.org/3/movie/{id}/credits?language=es-ES"

            response_movie_credits = requests.get(url2, headers=headers)

            response_movie_credits = response_movie_credits.json()
            print("\n\n")
            
#                print("Nombre:" , credit['name'])
#            for credit in response_movie_credits['cast']:
#                print("Profesión:", credit['character'])
#                print("Imágen: ", credit['profile_path'])
#                print("\n") 

            
            return render_template('movies/add-movie.html', response_movie=response_movie, response_movie_credits=response_movie_credits, id=id)

    return render_template('movies/add-movie.html')            

@app.route('/add-movie-rec/', methods=['GET', 'POST'])
def add_movie_rec():
    
    if request.method == 'POST':
        if request.form['movie_id']:
            id = request.form['movie_id']

            url = f"https://api.themoviedb.org/3/movie/{id}?language=es-ES"
            
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
            }
            
            response_movie = requests.get(url, headers=headers)
            response_movie = response_movie.json()
                        
        
    return render_template('movies/add-movie-rec.html', id=id, response_movie=response_movie)

@app.route('/add-movie-record', methods=['GET', 'POST'])
def add_movie_record():
    
    if request.method == 'POST':

        id = request.form['movie_id']
        url = f"https://api.themoviedb.org/3/movie/{id}?language=es-ES"
        
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
        }
            
        response_movie = requests.get(url, headers=headers)
        response_movie = response_movie.json()
             
                        
        file_video = request.files['file']
        filename = secure_filename(file_video.filename) #no es un error

        extension = os.path.splitext(filename)[1]
        nuevoNombre = response_movie['title'] + extension
        
        
        print(nuevoNombre)
        
        
    return redirect("/") 

@app.route('/movie-file', methods=['GET', 'POST'])
def movie_file():
    
    return render_template('movies/movie-file.html')
@app.route('/search-movie-file', methods=['GET', 'POST'])
def search_movie_file():
    
    if request.method == 'POST':
        file_video = request.files['file']
        filename = secure_filename(file_video.filename) #no es un error
        #extension = os.path.splitext(filename)[1]
        
        #Separamos la extensión y el nombre del fichero y dejamos el nombre sin la extensión
        filename_no_extension = os.path.splitext(filename)[0]
        filename_no_extension = filename_no_extension.replace('_', ' ')
        filename_no_extension = filename_no_extension.replace('.',' ')
        filename = filename_no_extension
        #Imprimimos el nombre de la película a buscar por consola
        print(f"Nombre de la película a buscar: " , filename_no_extension)
        
        #Buscamos el nombre de la película en DatamovieDB con su API
        search = filename_no_extension
        
        url = f"https://api.themoviedb.org/3/search/movie?query={search}&include_adult=false&language=es-ES&page=1"
            
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
        }
        
        response = requests.get(url, headers=headers)
        response = response.json()
         
        print(response)
        
        #Comprobamos si el nombre del archivo coincide con el nombre de la película en DatamovieDB
        if response['total_results'] == int(0):
            
            result = 0
            
            messageNotFound = "El nombre del archivo no coincide con el nombre de la película ó no se ha encontrado por este nombre en DatamovieDB"
            
            return render_template('movies/show-search-movie-file.html', response=response, filename=filename, result=result, messageNotFound=messageNotFound)
        else:
            return render_template('app/index.html', response=response, filename=filename)
        
    return render_template('movies/show-search-movie-file.html')

@app.route('/movie-rec', methods=['GET', 'POST'])
def movie_rec():
    
    if request.method == 'POST':
        if request.form['id']:
            id = request.form['id']

            url = f"https://api.themoviedb.org/3/movie/{id}?language=es-ES"
            
            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZTY5Njg1Zjg1ODMzNWU5MmI3NjM4NGNmYmE1OWIzZCIsInN1YiI6IjY2Mzc3ZGUzODNlZTY3MDEyZDQxY2Q0MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v4g7x6bSiDGvXvvab_WFpn2_m1rn3P3CE1wFUWbSAwE"
            }
            
            response_movie = requests.get(url, headers=headers)
            response_movie = response_movie.json()
            
            id_movie = response_movie['id']
            title = response_movie['title']
            overview = response_movie['overview']
            img = response_movie['poster_path']
            
            print(id, title, overview, img)
            
            connection = sqlite3.connect('database/myvideos.db')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO movies (id_movie, title, overview, img) VALUES (?, ?, ?, ?)", (id_movie, title, overview, img))
            connection.commit()
            cursor.close()
            connection.close()       
                        
    return render_template('/app/index.html', id=id, response_movie=response_movie)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>No se encuentra esta página</h1>", 404

if __name__ == '__main__':
    app.run(debug=True)

