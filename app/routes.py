from flask import send_from_directory

from app import app, socketio

# For simplicity, we'll just store the current ID in memory and increment it every
# time a message is received
messageID = 1


@app.route("/")
# HTTP handler to serve our single page app
def index():
    return send_from_directory('../client/public', 'index.html')


@app.route("/<path:path>")
# HTTP handler to serve static files (compiled JS/CSS, etc)
def static_files(path):
    return send_from_directory('../client/public', path)


@socketio.on('message')
# SocketIO event handler for handling our chat messages
def handle_message(data):
    global messageID

    data["id"] = messageID
    messageID += 1

    socketio.emit("message", data)
    print('received message: ' + data)
