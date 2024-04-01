#!/usr/bin/python3
"""
starts a Flask api application
"""

from flask import Flask
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
cors = CORS(app, origins='0.0.0.0')
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def endpoint_not_found(error):
    """Handle not found err."""
    return {"error": "Not found"}, 404


if __name__ == "__main__":
    """Starting Point of app"""
    host = getenv("HBNB_API_HOST")
    if not host:
        host = '0.0.0.0'
    port = getenv("HBNB_API_PORT")
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
