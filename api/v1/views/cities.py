#!/usr/bin/python3
"""
starts a Flask api application
"""

from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State
from flask import abort, request


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def get_cities(state_id):
    """Return status OK for status route"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    cities = []
    for city in state.cities:
        cities.append(city.to_dict())
    return cities, 200


@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """Return status OK for status route"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    return city.to_dict(), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def add_city(state_id):
    """Return status OK for status route"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    try:
        body = request.get_json()
    except Exception:
        abort(400, "Not a JSON")
    name = body.get('name')
    if not name:
        abort(400, "Missing name")
    city = City()
    city.name = name
    city.state_id = state_id
    city.save()
    return city.to_dict(), 201


@app_views.route('/cities/<city_id>', methods=['PUT'])
def edit_city(city_id):
    """Return status OK for status route"""
    forbidden = ['id', 'created_at', 'updated_at']
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    try:
        body = request.get_json()
    except Exception:
        abort(400, "Not a JSON")
    for key, val in body.items():
        if key not in forbidden:
            setattr(city, key, val)
    city.save()
    return city.to_dict(), 200


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def del_city(city_id):
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    storage.delete(city)
    storage.save()
    return {}, 200
