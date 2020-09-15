# -*- coding: utf-8 -*-
"""My Weather API that uses Flask framework and Current Weather API of OpenWeatherMap."""

import requests
import requests_cache
from flask import Flask, request, jsonify
#from flask_caching import Cache
import validators  # Functions to check variables and route args.
import webfunctions  # Functions to manipulate JSON and date time.

# Flask initialization
app = Flask(__name__)

# Load API settings of Current Weather API of OpenWeatherMap
app.config.from_pyfile('settings.py')

# JSON response configuration
app.config['JSON_SORT_KEYS'] = False  # Avoid unwanted JSON key order
app.config['JSON_AS_ASCII'] = False  # JSON in utf-8 format

# Cache initialization to mantain
requests_cache.install_cache('weather_cache', backend='sqlite', expire_after=120)
#cache = Cache()
#app.config['CACHE_TYPE'] = 'simple'
#cache.init_app(app)


#/weather?city=$City&country=$Country => API URL format to make the request
@app.route('/weather', methods=['GET'])
#@cache.cached(120)  # 2 minutes of cache. Doesn't captured the args changes :(
def weather():
    """The weather route of My Weather API."""
    # Load URL and KEY args of Current Weather API of OpenWeatherMap
    api_url = app.config.get("API_URL")
    api_key = app.config.get("API_KEY")
    validators.check_emptiness('API_URL', api_url)
    validators.check_emptiness('API_KEY', api_key)

    # Obtain and verify city and country args entered to route
    city = request.args.get('city')
    country = request.args.get('country')
    validators.check_emptiness('city', city)
    validators.check_emptiness('country', country)
    validators.check_regex('city', city, "[A-Za-z ]+")
    validators.check_regex('country', country, "[a-z]{2}")

    # Join the city and country args like input for 'request_ow_api' function
    place = webfunctions.get_place(city, country)

    # Obtain response from Current Weather API of OpenWeatherMap
    input_json = webfunctions.request_ow_api(api_url, api_key, place)

    # Debugging: print the 'input_json' data in good style
    # webfunctions.beautiful_json(input_json)

    # If 'input_json' hasn't HTTP:200 status,
    # then the response will be same that it was obtained from OpenWeatherMap
    webfunctions.reply_bad_response(input_json)

    # Create and return the final API response from My Weather API
    output_json = webfunctions.create_response_body(input_json)
    return jsonify(output_json)


if __name__ == '__main__':
    app.run()
