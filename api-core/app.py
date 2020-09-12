# -*- coding: utf-8 -*-
"""My weather API using a flask framework."""

import logging
from flask import Flask, request, jsonify, json, abort
from flask_caching import Cache
import checkconfig
import checkargs
import webfunctions
#from middleware import Middleware



logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False
cache = Cache()
app.config['CACHE_TYPE'] = 'simple'
cache.init_app(app)
#app.wsgi_app = Middleware(app.wsgi_app)


# /weather?city=$City&country=$Country
@app.route('/weather', methods=['GET'])
@cache.cached(timeout=10)
def weather():
    """Main function of Weather API."""
    logging.debug('Hello world - app.logger.info')

    # Load enviroment variables of OpenWeather API
    #api_url = app.config.get("API_URL")
    #api_key = app.config.get("API_KEY")

    # Files validation
    checkconfig.check_file('.flaskenv')
    checkconfig.check_file('.env')
    checkconfig.check_file('settings.py')

    # Capture of city and country args
    city = request.args.get('city', None)
    country = request.args.get('country', None)

    # Input args and their check section
    checkargs.check_empty('city', city)
    checkargs.check_empty('country', country)
    checkargs.check_arg('city', city, "[A-Za-z ]+", "string")
    checkargs.check_arg('country', country, "[a-z]{2}", "lower two letters")

    # Processing core API
    """
    place = webfunctions.get_place(city, country)
    try:
        owmap_response = webfunctions.request_ow_api(api_url, api_key, place)
    except:
        abort(500)
    input_json = json.loads(owmap_response)
    output_json = webfunctions.create_response_body(input_json)
    """
    output_json = webfunctions.get_random_num()
    return jsonify(output_json)


if __name__ == '__main__':
    app.run()
