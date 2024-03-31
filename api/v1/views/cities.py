#!/usr/bin/python3
"""
City Endpoints for the API
"""

from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State
from flask import abort, request


@app_views.route('/states/<state_id>/cities', methods=['GET', 'POST'])
def cities(state_id):
    """Return status OK for status route"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if request.method == 'GET':
        cities = []
        for city in state.cities:
            cities.append(city.to_dict())
        return cities, 200
    if request.method == 'POST':
        try:
            body = request.get_json()
        except Exception:
            abort(400, "Not a JSON")
        name = body.get('name')
        if not name:
            abort(400, "Missing name")
        city = City(**body)
        city.save()
        return city.to_dict(), 201


@app_views.route('/cities/<city_id>', methods=['GET', 'PUT', 'DELETE'])
def city_id(city_id):
    """Return status OK for status route"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    if request.method == "GET":
        return city.to_dict(), 200
    if request.method == 'PUT':
        forbidden = ['id', 'created_at', 'updated_at']
        try:
            body = request.get_json()
        except Exception:
            abort(400, "Not a JSON")
        for key, val in body.items():
            if key not in forbidden:
                setattr(city, key, val)
        city.save()
        return city.to_dict(), 200
    if request.method == "DELETE":
        storage.delete(city)
        storage.save()
        return {}, 200
