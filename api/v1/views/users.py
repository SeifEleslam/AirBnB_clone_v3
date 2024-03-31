#!/usr/bin/python3
"""
starts a Flask api application
"""

from api.v1.views import app_views
from models import storage
from models.user import User
from flask import abort, request


@app_views.route('/users', methods=['GET'])
def get_users():
    """Return status OK for status route"""
    users = []
    for user in storage.all(User).values():
        users.append(user.to_dict())
    return users, 200


@app_views.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Return status OK for status route"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return user.to_dict(), 200


@app_views.route('/users', methods=['POST'])
def add_user():
    """Return status OK for status route"""
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
    user = User()
    user.email = email
    user.password = password
    user.save()
    return user.to_dict(), 201


@app_views.route('/users/<user_id>', methods=['PUT'])
def edit_user(user_id):
    """Return status OK for status route"""
    forbidden = ['id', 'created_at', 'updated_at', 'email']
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    try:
        body = request.get_json()
    except Exception:
        abort(400, "Not a JSON")
    for key, val in body.items():
        if key not in forbidden:
            setattr(user, key, val)
    user.save()
    return user.to_dict(), 200


@app_views.route('/users/<user_id>', methods=['DELETE'])
def del_user(user_id):
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return {}, 200
