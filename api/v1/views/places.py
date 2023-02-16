#!/usr/bin/python3
"""
Route definitions for 'places' view
"""
from api.v1.views import app_views
from flask import request, jsonify, make_response, abort
from models import storage
from models.city import City
from models.place import Place
from models.user import User


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def list_places(city_id):
    """Returns a list of places in a given city"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    places_list = [place.to_dict() for place in city.places]

    return jsonify(places_list)


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_place(place_id):
    """Returns a specific place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """Deletes a specific place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    storage.delete(place)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    """Creates a new place in the given city"""
    if not request.is_json:
        abort(400, 'Not a JSON')
    if 'user_id' not in request.get_json():
        abort(400, 'Missing user_id')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')

    data = request.get_json()
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    data['city_id'] = city_id
    user = storage.get(User, data['user_id'])
    if user is None:
        abort(404)

    new_place = Place(**data)
    new_place.save()

    return make_response(jsonify(new_place.to_dict()), 201)


@app_views.route('/places/<place_id>', methods=['PUT'],
                 strict_slashes=False)
def update_place(place_id):
    """Updates a place's record"""
    if not request.is_json:
        abort(400, 'Not a JSON')

    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    data = request.get_json()
    ignore = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']

    for key, value in data.items():
        if key not in ignore:
            setattr(place, key, value)
    storage.save()

    return make_response(jsonify(place.to_dict()), 200)
