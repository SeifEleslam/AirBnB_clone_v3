#!/usr/bin/python3
"""
review Endpoints for the API
"""

from api.v1.views import app_views
from models import storage
from models.place import Place
from models.user import User
from models.review import Review
from flask import abort, request, jsonify


@app_views.route('/places/<place_id>/reviews', methods=['GET', 'POST'])
def reviews(place_id):
    """Return status OK for status route"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    if request.method == 'GET':
        reviews = []
        for review in place.reviews:
            reviews.append(review.to_dict())
        return jsonify(reviews), 200
    if request.method == 'POST':
        try:
            body = request.get_json()
        except Exception:
            abort(400, "Not a JSON")
        if not body.get('user_id'):
            abort(400, "Missing user_id")
        if not storage.get(User, body.get('user_id')):
            abort(404)
        if not body.get('text'):
            abort(400, "Missing text")
        review = Review(**body)
        review.save()
        return review.to_dict(), 201


@app_views.route('/reviews/<review_id>', methods=['GET', 'PUT', 'DELETE'])
def review_id(review_id):
    """Return status OK for status route"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    if request.method == "GET":
        return review.to_dict(), 200
    if request.method == 'PUT':
        forbidden = ['id', 'created_at', 'updated_at', 'place_id', 'user_id']
        try:
            body = request.get_json()
        except Exception:
            abort(400, "Not a JSON")
        for key, val in body.items():
            if key not in forbidden:
                setattr(review, key, val)
        review.save()
        return review.to_dict(), 200
    if request.method == "DELETE":
        storage.delete(review)
        storage.save()
        return {}, 200
