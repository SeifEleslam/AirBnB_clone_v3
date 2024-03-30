#!/usr/bin/python3
"""
starts a Flask api application
"""

from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def ok_status():
    """Return status OK for status route"""
    return {"status": "OK"}, 200


@app_views.route('/stats')
def stats():
    """Return status OK for status route"""
    from models.engine.db_storage import classes
    json_res = dict()
    print(sorted(classes))
    for key in sorted(classes):
        json_res[classes[key].__tablename__] = storage.count(classes[key])
    return json_res, 200
