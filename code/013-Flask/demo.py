# pip install flask
# flask --version
# flask which

# Importing Flask
from flask import Flask, request

app = Flask(__name__)

# Basic Route - The web server listens for a specific URL to be sent
# Does a function when that URL is triggered

@app.route("/hello")
def hello():
    return "make a second route that listens for /html and sends a h2 header"

@app.route("/html")
def html():
    return "<h2> Hello World! </h2>"

@app.route("/gif")
def html_2():
    # return -> Outputting some data back to the browser
    return "<img src='https://picsum.photos/200' alt='random pic'>"

# Url Query, Param queries, Body Requests
@app.route("/query/<search>")
def search_query(search):
    # data = db.query("SELECT * FROM data")
    # return data
    return f"You have searched for {search}.. Sorry, no results :( "

@app.route("/movies/create", methods=['POST'])
def createMovie():
    data = request.get_json()
    print(data['title']) # Populate and create objects
    return data, 210

class movie:

    def __init__(self, title, rating, cast):
        self.title = title
        self.rating = rating
        self.cast = cast

# To run the app:
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)