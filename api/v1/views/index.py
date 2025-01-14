#!/usr/bin/python3
"""This module implement a rule that
returns the status of the application"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def status():
    """View function that return a json message"""
    state = {
        "status": "OK"
    }
    return (jsonify(state))


@app_views.route('/stats')
def stats():
    """endpoint that retrieves the number of each objects by type"""
    total_classes = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User),
    }
    return (jsonify(total_classes))
