#!/usr/bin/python3
"""
Route definitions for the apps index views.
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def return_status():
    """Returns OK status JSON response"""
    return jsonify(status='OK')
