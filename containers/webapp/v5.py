from flask import Flask
import datetime

app = Flask(__name__)


@app.route('/')
def main():
    current_datetime = datetime.datetime.now()
    return f'hello world, v5 {current_datetime}'


@app.route('/health')
def health():
    return 'OK'


@app.route("/greeting")
def greeting():
    return 'hi!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
