import socket

from flask_socketio import SocketIO, emit, send
from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from wsgiref import simple_server
import os

app = Flask(__name__)
CORS(app)
socket_io = SocketIO(app, cors_allowed_origins="*")


@socket_io.on('connect', namespace="/test")
def printsocket():
    print("Connected")
    emit('connection', {'data':"Established socket connection for connect"})


@socket_io.on('button_clicked', namespace="/test")
def buttonclicked(data):
    print(data)
    emit("data_found", data)
    print(data['name'])


@app.route("/", methods=["GET", "POST"])
@cross_origin()
def hello():
    hi = "Hello"
    return render_template('index.html', msg=hi)


#
# if __name__ == "__main__":
#     socket_io.run(app)

#
# # port = int(os.getenv("PORT",5001))
# if __name__ == "__main__":
#     # host = '0.0.0.0'
#     # #port = 5000
#     #
#     # httpd = simple_server.make_server(host, port, app)
#     # #print("Serving on %s %d" % (host, port))
#     # httpd.serve_forever()
#     socket_io.run(app, host='0.0.0.0')


port = int(os.getenv("PORT", 5001))
is_local_run=False

if __name__ == "__main__" and is_local_run:
    app.run()
if __name__ == "__main__" and not is_local_run:
    # host = '0.0.0.0'
    # httpd = simple_server.make_server(host, port, app)
    # httpd.serve_forever()
    socket_io.run(app,host='0.0.0.0',port=5000)