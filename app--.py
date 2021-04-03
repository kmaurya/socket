import time

from flask import Flask, Response


app = Flask(__name__)


@app.route('/')
def index():
    def gen():
        for c in 'Hello world!':
            yield c
            time.sleep(1)
    return Response(gen())


if __name__ == '__main__':
    app.run()