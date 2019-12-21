from flask import Flask
import datetime
import os

app = Flask(__name__)


@app.route('/')
def main():
    current_datetime = datetime.datetime.now()
    message = os.environ.get('MESSAGE')
    return f'hello world, v5 {current_datetime} { message }'


@app.route('/health')
def health():
    return 'OK'


@app.route("/greeting")
def greeting():
    return 'hi!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
