# pip install flask
# flask --version
# flask which

# Importing Flask
from flask import Flask

app = Flask(__name__)

# Basic Route - The web server listens for a specific URL to be sent
# Does a function when that URL is triggered

@app.route("/hello")
def hello():
    return "Whaytever text we send this will work"


# To run the app:
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)