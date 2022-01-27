from flask import send_from_directory
from app import app


@app.route("/")
def index():
    return send_from_directory('../client/public', 'index.html')


@app.route("/<path:path>")
def home(path):
    # static files (compiled JS/CSS, etc)
    return send_from_directory('../client/public', path)


@app.route("/hello")
def hello():
    return 'hello world'
