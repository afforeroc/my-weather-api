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


def check_city_country(city_prev, city, country_prev, country):
    print(city_prev)
    print(city)
    print(country_prev)
    print(country)
    """
    if city_prev != city or country_prev != country:
        city_prev = city
        country_prev = country_prev
        with app.app_context():
            cache.init_app(app)
    """

#/weather?city=$City&country=$Country
@app.route('/weather', methods=['GET'])
#@cache.cached(120)
def weather():
    """Main function of Weather API."""
    # Load URL and KEY of OpenWeather API
    api_url = app.config.get("API_URL")
    api_key = app.config.get("API_KEY")
    check_emptiness('API_URL', api_url)
    check_emptiness('API_KEY', api_key)
    
    city = request.args.get('city', None)
    country = request.args.get('country', None)

    check_emptiness('city', city)
    check_emptiness('country', country)
    check_regex('city', city, "[A-Za-z ]+")
    check_regex('country', country, "[a-z]{2}")

    # Processing core API
    place = webfunctions.get_place(city, country)


    cache_status = webfunctions.refresh_cache('.cache', city, country)
    try:
        if cache_status:
            owmap_response = webfunctions.request_ow_api(api_url, api_key, place)
    except:
        print("error")
    
    
    input_json = json.loads(owmap_response)
    #webfunctions.beautiful_json(input_json)
    output_json = webfunctions.create_response_body(input_json)
    return jsonify(output_json)


if __name__ == '__main__':
    app.run()
