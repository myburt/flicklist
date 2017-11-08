from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    movie2 = get_random_movie()
    movie3 = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"
    content += "<h2>Tommorows Movie</h2>"
    content += "<ul>"
    content += "<li>" + movie2 + "</li>"
    content += "<li>" + movie3 + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"

    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movie_list = ["Dude where's my car", "Ghost Busters", "Austin Powers", "Hell Raiser", "Crouching Tiger Hidden Dragon",
    "Anchorman", "Shrek", "Lord of the Rings", "Finding Nemo"]
    # TODO: randomly choose one of the movies, and return it
    return movie_list[random.randrange(0, len(movie_list))]


app.run()
