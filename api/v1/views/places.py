#!/usr/bin/python3
"""
Place Endpoints for the API
"""

from api.v1.views import app_views
from models import storage
from models.city import City
from models.place import Place
from models.state import State
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


@app_views.route('/places_search', methods=['POST'])
def search_places():
    """Return status OK for status route"""
    try:
        body = request.get_json()
    except Exception:
        abort(400, "Not a JSON")
    states_ids = body.get('states', [])
    cities_ids = body.get('cities', [])
    amenities_ids = body.get('amenities', [])
    for id in states_ids:
        state = storage.get(State, id)
        if state:
            cities_ids = list(
                set(cities_ids + [city.id for city in state.cities]))

    places = storage.all(Place).values()
    out_places = []
    for place in places:
        place_amenities = [amenity.id for amenity in place.amenities]
        if (not (body.get('states') or body.get('cities')
                 ) or place.city_id in cities_ids) and all(
                amenity in place_amenities for amenity in amenities_ids):
            dic = place.to_dict()
            if dic.get('amenities'):
                dic['amenities'] = [amenity.to_dict()
                                    for amenity in dic['amenities']]
            out_places.append(dic)
    return jsonify(out_places), 200
