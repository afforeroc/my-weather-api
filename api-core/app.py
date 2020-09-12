# -*- coding: utf-8 -*-
"""My weather API using a flask framework."""

import logging
from datetime import datetime
from flask import Flask, request, jsonify, json, abort
from flask_caching import Cache
from validators import check_emptiness, check_regex
import webfunctions
import os
#from middleware import Middleware

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False
cache = Cache()
app.config['CACHE_TYPE'] = 'simple'
cache.init_app(app)

#/weather?city=$City&country=$Country
@app.route('/weather', methods=['GET'])
@cache.cached(timeout=120)
def weather():
    """Main function of Weather API."""

    # Load URL and KEY of OpenWeather API
    api_url = app.config.get("API_URL")
    api_key = app.config.get("API_KEY")
    check_emptiness('API_URL', api_url)
    check_emptiness('API_KEY', api_key)

    # Capture of city and country args
    city = request.args.get('city', None)
    country = request.args.get('country', None)
    check_emptiness('city', city)
    check_emptiness('country', country)
    check_regex('city', city, "[A-Za-z ]+")
    check_regex('country', country, "[a-z]{2}")

    # Processing core API
    place = webfunctions.get_place(city, country)
    try:
        owmap_response = webfunctions.request_ow_api(api_url, api_key, place)
    except:
        abort(500)
    input_json = json.loads(owmap_response)
    output_json = webfunctions.create_response_body(input_json)
    return jsonify(output_json)


if __name__ == '__main__':
    app.run()
