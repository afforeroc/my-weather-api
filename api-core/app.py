# -*- coding: utf-8 -*-
"""My weather API using a flask framework."""
import json
from flask import Flask, request, jsonify
import webfunctions
from loggermiddleware import Middleware

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False
app.config.from_pyfile('settings.py')


# /weather?city=$City&country=$Country
@app.route('/weather', methods=['GET'])
def weather():
    """Main function of Weather API."""
    app.wsgi_app = Middleware(app.wsgi_app)

    # Files validator
    webfunctions.check_file('.flaskenv')
    webfunctions.check_file('.env')
    webfunctions.check_file('settings.py')

    # Check main args: city and country
    city = request.args.get('city', None)
    country = request.args.get('country', None)
    webfunctions.check_empty('city', city)
    webfunctions.check_empty('country', country)
    webfunctions.check_city(city)
    webfunctions.check_country(country)

    # Args transformation
    city = str(city).replace(' ', '%20')
    country = str(country)

    # Load env variables
    api_url = app.config.get("API_URL")
    api_key = app.config.get("API_KEY")

    # Core functions
    city_country = f"{city},{country}"
    owmap_response = webfunctions.openweathermap_api(api_url, api_key,
                                                     city_country)
    input_json = json.loads(owmap_response)
    output_json = webfunctions.create_response_body(input_json)
    return jsonify(output_json)


if __name__ == '__main__':
    app.run()
