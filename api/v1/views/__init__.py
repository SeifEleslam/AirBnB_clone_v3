#!/usr/bin/python3
"""
start Blueprint
"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')

if app_views:
    import api.v1.views.index
    import api.v1.views.states
