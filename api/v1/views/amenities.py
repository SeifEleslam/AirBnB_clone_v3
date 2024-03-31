#!/usr/bin/python3
"""
starts a Flask api application
"""

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from flask import abort, request


@app_views.route('/amenities', methods=['GET'])
def get_amenities():
    """Return status OK for status route"""
    amenities = []
    for amenity in storage.all(Amenity).values():
        amenities.append(amenity.to_dict())
    return amenities, 200


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """Return status OK for status route"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    return amenity.to_dict(), 200


@app_views.route('/amenities', methods=['POST'])
def add_amenity():
    """Return status OK for status route"""
    try:
        body = request.get_json()
    except Exception:
        abort(400, "Not a JSON")
    name = body.get('name')
    if not name:
        abort(400, "Missing name")
    amenity = Amenity()
    amenity.name = name
    amenity.save()
    return amenity.to_dict(), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def edit_amenity(amenity_id):
    """Return status OK for status route"""
    forbidden = ['id', 'created_at', 'updated_at']
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    try:
        body = request.get_json()
    except Exception:
        abort(400, "Not a JSON")
    for key, val in body.items():
        if key not in forbidden:
            setattr(amenity, key, val)
    amenity.save()
    return amenity.to_dict(), 200


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def del_amenity(amenity_id):
    """Delete an existing amenity."""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return {}, 200
