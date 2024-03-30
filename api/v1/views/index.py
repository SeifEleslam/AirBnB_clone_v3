#!/usr/bin/python3
"""
starts a Flask api application
"""

from api.v1.views import app_views


@app_views.route('/status')
def ok_status():
    return {"status": "OK"}
