#!/usr/bin/python3
"""
review Endpoints for the API
"""

from api.v1.views import app_views
from models import storage
from models.place import Place
from models.amenity import Amenity
from flask import abort, request, jsonify


@app_views.route('/places/<place_id>/amenities', methods=['GET'])
def place_amenities(place_id):
    """Return status OK for status route"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenities = []
    for amenity in place.amenities:
        amenities.append(amenity.to_dict())
    return jsonify(amenities), 200


@app_views.route('places/<place_id>/amenities/<amenity_id>', methods=['POST', 'DELETE'])
def place_amenity_id(place_id, amenity_id):
    """Return status OK for status route"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if request.method == 'POST':
        if amenity in place.amenities:
            return jsonify(amenity.to_dict()), 200
        place.amenities.append(amenity)
        storage.save()
        return jsonify(amenity.to_dict()), 201
    if request.method == "DELETE":
        if amenity not in place.amenities:
            abort(404)
        place.amenities.remove(amenity)
        storage.save()
        return jsonify({}), 200
