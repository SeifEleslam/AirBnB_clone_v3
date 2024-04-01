#!/usr/bin/python3
"""
User Endpoints for the API
"""

from api.v1.views import app_views
from models import storage
from models.user import User
from flask import abort, request, jsonify


@app_views.route('/users', methods=['GET', 'POST'])
def users():
    """Return status OK for status route"""
    if request.method == 'GET':
        users = []
        for user in storage.all(User).values():
            users.append(user.to_dict())
        return jsonify(users), 200
    if request.method == 'POST':
        try:
            body = request.get_json()
        except Exception:
            abort(400, "Not a JSON")
        email = body.get('email')
        if not email:
            abort(400, "Missing email")
        password = body.get('password')
        if not password:
            abort(400, "Missing password")
        user = User(**body)
        user.save()
        return user.to_dict(), 201


@app_views.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_id(user_id):
    """Return status OK for status route"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if request.method == "GET":
        return user.to_dict(), 200
    if request.method == "PUT":
        forbidden = ['id', 'created_at', 'updated_at', 'email']
        try:
            body = request.get_json()
        except Exception:
            abort(400, "Not a JSON")
        for key, val in body.items():
            if key not in forbidden:
                setattr(user, key, val)
        user.save()
        return user.to_dict(), 200
    if request.method == "DELETE":
        storage.delete(user)
        storage.save()
        return {}, 200
