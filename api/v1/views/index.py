#!/usr/bin/python3
"""status and stats of a Flask api application"""

from api.v1.views import app_views
from models import storage
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def ok_status():
    """Return status OK for status route"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """Return status OK for status route"""
    from models.engine.db_storage import classes
    json_res = dict()
    print(sorted(classes))
    for key in sorted(classes):
        json_res[classes[key].__tablename__] = storage.count(classes[key])
    return jsonify(json_res), 200
