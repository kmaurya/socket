import socket
from flask_socketio import SocketIO, emit, send
from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
socket_io = SocketIO(app, cors_allowed_origins="*")


@socket_io.on('connect', namespace="/test")
def printsocket():
    print("Connected")
    # emit('connection', "Established socket connection for connect")


@socket_io.on('button_clicked', namespace="/test")
def buttonclicked(data):
    print(data)
    # emit("data_found",data)
    print(data['name'])


@app.route("/", methods=["GET", "POST"])
@cross_origin()
def hello():
    hi = "Hello"
    return render_template('index.html', msg=hi)


if __name__ == "__main__":
    socket_io.run(app)
