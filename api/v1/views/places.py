#!/usr/bin/python3
"""
Place Endpoints for the API
"""

from api.v1.views import app_views
from models import storage
from models.city import City
from models.place import Place
from models.user import User
from flask import abort, request, jsonify


@app_views.route('/cities/<city_id>/places', methods=['GET'])
def get_places(city_id):
    """Return status OK for status route"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    places = []
    for place in city.places:
        places.append(place.to_dict())
    return jsonify(places), 200


@app_views.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    """Return status OK for status route"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict()), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'])
def add_place(city_id):
    """Return status OK for status route"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    try:
        body = request.get_json()
    except Exception:
        abort(400, "Not a JSON")
    user_id = body.get('user_id')
    if not user_id:
        abort(400, "Missing user_id")
    if not storage.get(User, user_id):
        abort(404)
    name = body.get('name')
    if not name:
        abort(400, "Missing name")
    place = Place()
    place.user_id = user_id
    place.city_id = city_id
    place.name = name
    place.save()
    return jsonify(place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'])
def edit_place(place_id):
    """Return status OK for status route"""
    forbidden = ['id', 'created_at', 'updated_at', 'user_id', 'city_id']
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    try:
        body = request.get_json()
    except Exception:
        abort(400, "Not a JSON")
    for key, val in body.items():
        if key not in forbidden:
            setattr(place, key, val)
    place.save()
    return jsonify(place.to_dict()), 200


@app_views.route('/places/<place_id>', methods=['DELETE'])
def del_place(place_id):
    """Delete an existing place."""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({}), 200
