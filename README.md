# flask-svelte-chat

A simple real-time chat app built with [Flask](https://flask.palletsprojects.com/en/2.0.x/), [Svelte](https://svelte.dev/), and [SocketIO](https://socket.io/).

## Getting Started

```sh
# From root of this repo...
python3 -m venv ./venv # create virtual environment
source venv/bin/activate  # "activate" virtual environment
pip install -r requirements.txt # install python deps
flask run # run backend server (watches files for changes)

# In another terminal...
cd client # our frontend code is in the client directory
yarn # install frontend deps
yarn dev # run frontend build task (watches files for changes)
```

## Usage

Once you have the app running, you should be able to access it at [localhost:5000/](http://localhost:5000/). Try opening it in two separate browser tabs and sending some messages. You should be able to switch between tabs and see the messages appear, without any need for a page refresh.
