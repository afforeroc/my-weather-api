# -*- coding: utf-8 -*-
"""My weather API using a flask framework."""

import logging
from flask import Flask, request, jsonify, json, abort, Response
from flask_caching import Cache
import validators  # Functions to check variables and route args.
import webfunctions  # Functions to manipulate JSON and date time.


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
#@cache.cached(120)
def weather():
    """Main function of Weather API."""
    # Load URL and KEY of OpenWeather API
    api_url = app.config.get("API_URL")
    api_key = app.config.get("API_KEY")
    validators.check_emptiness('API_URL', api_url)
    validators.check_emptiness('API_KEY', api_key)

    # Obtain and verify the city and country args
    city = request.args.get('city', None)
    country = request.args.get('country', None)
    validators.check_emptiness('city', city)
    validators.check_emptiness('country', country)
    validators.check_regex('city', city, "[A-Za-z ]+")
    validators.check_regex('country', country, "[a-z]{2}")

    # Processing core API
    place = webfunctions.get_place(city, country)
    input_json = webfunctions.request_ow_api(api_url, api_key, place)
    print(">>>>>>>>>>>>", input_json['cod'], type(input_json['cod']))
    if str(input_json['cod']) != '200':
        code = int(input_json['cod'])
        message = str(input_json['message'])
        abort(Response(message, code))
    else:
        webfunctions.beautiful_json(input_json)
        output_json = webfunctions.create_response_body(input_json)
        return jsonify(output_json)


if __name__ == '__main__':
    app.run()
