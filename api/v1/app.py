#!/usr/bin/python3
"""
app.py - contains the app instantiation.
"""
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from os import getenv


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db_connection(exc):
    """Close current DB session"""
    storage.close()


@app.errorhandler(404)
def handle_404_error(err):
    """Return 404 JSON error message"""
    return jsonify(error='Not found'), 404


if __name__ == '__main__':
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
