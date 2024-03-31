#!/usr/bin/python3
"""
State Endpoints for the API
"""

from api.v1.views import app_views
from models import storage
from models.state import State
from flask import abort, request


@app_views.route('/states', methods=['GET'])
def get_states():
    """Return status OK for status route"""
    states = []
    for state in storage.all(State).values():
        states.append(state.to_dict())
    return states, 200


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """Return status OK for status route"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return state.to_dict(), 200


@app_views.route('/states', methods=['POST'])
def add_state():
    """Return status OK for status route"""
    try:
        body = request.get_json()
    except Exception:
        abort(400, "Not a JSON")
    name = body.get('name')
    if not name:
        abort(400, "Missing name")
    state = State()
    state.name = name
    state.save()
    return state.to_dict(), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def edit_state(state_id):
    """Return status OK for status route"""
    forbidden = ['id', 'created_at', 'updated_at']
    state = storage.get(State, state_id)
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
    return state.to_dict(), 200


@app_views.route('/states/<state_id>', methods=['DELETE'])
def del_state(state_id):
    """Delete an existing state."""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return {}, 200
