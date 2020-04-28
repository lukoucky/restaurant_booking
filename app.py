import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, RestaurantTable

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    if 'DATABASE_URL' in os.environ:
        setup_db(app, os.environ['DATABASE_URL'])
    else:
        setup_db(app)
    CORS(app)

    @app.route('/')
    def index():
        return 'Hello from Heroku, env variable: ' + os.environ['ENV_VALUE']

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
