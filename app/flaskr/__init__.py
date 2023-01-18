import json
import os

import requests
from flask import Flask, render_template, request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/wrefijdvov')
    def hello():
        return 'Hello, World!'

    @app.route('/', methods=('GET', 'POST'))
    def home():
        request=requests.get('https://fortnite-api.com/v2/shop/br').text
        api=json.loads(request)
        return render_template('index.html')

    @app.route('/', methods=('GET', 'POST'))
    def getPost():
        request=requests.get("https://fortnite-api.com/v1/banners/colors").text
        api=json.loads(request)
        return render_template('test.html',api=api)
    return app

    