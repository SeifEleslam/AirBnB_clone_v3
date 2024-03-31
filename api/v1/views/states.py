#!/usr/bin/python3
"""
State Endpoints for the API
"""

from api.v1.views import app_views
from models import storage
from models.state import State
from flask import abort, request, jsonify


@app_views.route('/states', methods=['GET', 'POST'])
def states():
    """Return status OK for status route"""
    if request.method == 'GET':
        states = []
        for state in storage.all(State).values():
            states.append(state.to_dict())
        return states, 200
    if request.method == "POST":
        try:
            body = request.get_json()
        except Exception:
            abort(400, "Not a JSON")
        name = body.get('name')
        if not name:
            abort(400, "Missing name")
        state = State(**body)
        state.save()
        return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['GET', 'PUT', 'DELETE'])
def state_id(state_id):
    """Return status OK for status route"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if request.method == 'GET':
        return jsonify(state.to_dict()), 200
    if request.method == 'PUT':
        forbidden = ['id', 'created_at', 'updated_at']
        if not state:
            abort(404)
        try:
            body = request.get_json()
        except Exception:
            abort(400, "Not a JSON")
        for key, val in body.items():
            if key not in forbidden:
                setattr(state, key, val)
        state.save()
        return jsonify(state.to_dict()), 200
    if request.method == 'DELETE':
        storage.delete(state)
        storage.save()
        return {}, 200
