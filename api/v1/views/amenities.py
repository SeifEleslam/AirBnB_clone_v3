#!/usr/bin/python3
"""
Amenity Endpoints for the API
"""

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from flask import abort, request, jsonify


@app_views.route('/amenities', methods=['GET', 'POST'])
def amenities():
    """Return status OK for status route"""
    if request.method == "GET":
        amenities = []
        for amenity in storage.all(Amenity).values():
            amenities.append(amenity.to_dict())
        return jsonify(amenities), 200
    if request.method == "POST":
        try:
            body = request.get_json()
        except Exception:
            abort(400, "Not a JSON")
        name = body.get('name')
        if not name:
            abort(400, "Missing name")
        amenity = Amenity(**body)
        amenity.save()
        return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['GET', 'PUT', 'DELETE'])
def amenity_id(amenity_id):
    """Return status OK for status route"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if request.method == "GET":
        return jsonify(amenity.to_dict()), 200
    if request.method == "PUT":
        forbidden = ['id', 'created_at', 'updated_at']
        try:
            body = request.get_json()
        except Exception:
            abort(400, "Not a JSON")
        for key, val in body.items():
            if key not in forbidden:
                setattr(amenity, key, val)
        amenity.save()
        return jsonify(amenity.to_dict()), 200
    if request.method == "DELETE":
        storage.delete(amenity)
        storage.save()
        return jsonify({}), 200
