from flask import Flask
application = app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Python! ci cd completed'

if __name__ == '__main__':
    app.run()