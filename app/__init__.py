from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


def run():
    socketio.run(app)


from app import routes  # nopep8
