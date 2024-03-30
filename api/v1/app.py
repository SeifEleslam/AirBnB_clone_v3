#!/usr/bin/python3
"""
starts a Flask api application
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    """Starting Point of app"""
    host = getenv("HBNB_API_HOST")
    host = '0.0.0.0' if not host else host
    port = getenv("HBNB_API_PORT")
    port = '5000' if not port else port
    app.run(host=host, port=port)
