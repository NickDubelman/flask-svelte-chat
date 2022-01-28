from flask import send_from_directory

from app import app, socketio

messageID = 1


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


@socketio.on('message')
def handle_message(data):
    global messageID

    data["id"] = messageID
    messageID += 1

    socketio.emit("message", data)
    print('received message: ' + data)
