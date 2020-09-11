# -*- coding: utf-8 -*-
"""My weather API using a flask framework."""
import os
import json
import datetime
import urllib.request
import re
from dotenv import load_dotenv
from flask import Flask, abort, request, jsonify
from loggermiddleware import LoggerMiddleware


def check_file(pathfile):
    """Check if a pathfile exists and is not empty."""
    if not os.path.isfile(pathfile):
        print(f"Oops! '{pathfile}' was not found")
        abort(404)

    if os.stat(pathfile).st_size == 0:
        print(f"Oops! '{pathfile}' is empty")
        abort(404)


def check_args(*args):
    """Check if the args are not None or empty."""
    for i, arg in enumerate(args):
        print(arg)
        if arg is None or arg == '':
            print(f"Oops! arg[{i}] is None or empty")
            abort(400)


def check_city(city):
    """Check if 'city' arg is a string composed only by with letters."""
    city_str = str(city)
    reg_expr = "[A-Za-z ]+" # String composed only by with letters
    pattern = re.compile(reg_expr)
    if pattern.fullmatch(city) is None:
        print("Bad request by wrong syntax")
        print(f"Oops! city => '{city_str}' not match with '{reg_expr}' regex expression")
        abort(400)
    else:
        print(f"city => '{city_str}', city arg:\tOK")


def check_country(country):
    """Check if 'country' arg is a lower string with only two letters."""
    country_str = str(country)
    reg_expr = "[a-z]{2}" # Lower string with only two letters
    pattern = re.compile(reg_expr)
    if pattern.fullmatch(country_str) is None:
        print("----------------------")
        print("BAD ARGUMENT")
        print(f"Oops! country => '{country_str}' not match with '{reg_expr}' regex expression")
        print("----------------------")
        abort(400)
    else:
        print(f"country => '{country_str}', country arg:\tOK")


def openweathermap_api(api_url, api_key, city_country):
    """Request weather data from OpenWeatherMap."""
    # source contain json data from api
    json_data = urllib.request.urlopen(api_url + city_country + 
                                        '&units=metric&appid=' + 
                                        api_key).read()
    return json_data


def beautiful_json(data_json):
    """Print in console a JSON data in beautiful style."""
    json_data = json.dumps(data_json, indent=4,
                           ensure_ascii=False, sort_keys=False).encode('utf8')
    print(json_data.decode())


def get_location_name(input_json):
    """Construct the location name with city and country."""
    city = str(input_json['name'])
    country_code = str(input_json['sys']['country'])
    location_name = f"{city}, {country_code}"
    return location_name


def get_temperature(input_json):
    """Concatenate the celius value with its unit of measurement."""
    celsius_deg = str(input_json['main']['temp'])
    return f"{celsius_deg} °C"


def get_wind(input_json):
    """Concatenate all wind values with their units of measurement."""
    wind_speed = float(input_json['wind']['speed'])
    wind_deg = int(input_json['wind']['deg'])
    wind_deg = int(input_json['wind']['deg'])
    wind = f"{wind_speed} m/s, {wind_deg} deg"
    return wind


def get_humidity(input_json):
    """Concatenate the humidity value with its unit of measurement."""
    humidity_val = str(input_json['main']['humidity'])
    humidity = f"{humidity_val}%"
    return humidity


def get_pressure(input_json):
    """Concatenate the humidity value with its unit of measurement."""
    pressure_val = str(input_json['main']['pressure'])
    pressure = f"{pressure_val} hPa"
    return pressure


def get_cloudines(input_json):
    """..."""
    clouds_val = int(input_json['clouds']['all'])
    cloudines = ''
    if 11 <= clouds_val < 25:
        cloudines = 'Few clouds'
    elif 25 <= clouds_val < 50:
        cloudines = 'Scattered clouds'
    elif 50 <= clouds_val < 85:
        cloudines = 'Broken clouds'
    elif 85 <= clouds_val <= 100:
        cloudines = 'Overcast clouds'
    return cloudines


def get_coordinates(input_json):
    """..."""
    coord_lon = str(input_json['coord']['lon'])
    coord_lat = str(input_json['coord']['lat'])
    geo_coordinates = [coord_lat, coord_lon]
    return geo_coordinates


def get_sunrise_sunset(input_json):
    """..."""
    sunrise_ut = int(input_json['sys']['sunrise'])
    sunset_ut = int(input_json['sys']['sunset'])

    sunrise_ts = datetime.datetime.fromtimestamp(sunrise_ut)
    sunset_ts = datetime.datetime.fromtimestamp(sunset_ut)

    sunrise = sunrise_ts.strftime('%H:%M')
    sunset = sunset_ts.strftime('%H:%M')
    return sunrise, sunset


def get_requested_time(input_json):
    """..."""
    requested_ut = int(input_json['dt'])
    requested_ts = datetime.datetime.fromtimestamp(requested_ut)
    requested_time = requested_ts.strftime('%Y-%m-%d %H:%M:%S')
    return requested_time


def create_response_body(input_json):
    """..."""
    location_name = get_location_name(input_json)
    temperature = get_temperature(input_json)
    wind = get_wind(input_json)
    cloudines = get_cloudines(input_json)
    humidity = get_humidity(input_json)
    pressure = get_pressure(input_json)
    sunrise, sunset = get_sunrise_sunset(input_json)
    geo_coordinates = get_coordinates(input_json)
    requested_time = get_requested_time(input_json)

    output_json = {
        "location_name": location_name,
        "temperature": temperature,
        "wind": wind,
        "cloudines": cloudines,
        "pressure": pressure,
        "humidity": humidity,
        "sunrise": sunrise,
        "sunset": sunset,
        "geo_coordinates": geo_coordinates,
        "requested_time": requested_time
    }
    #output_json = json.dumps(json_response, indent=4, sort_keys=False)
    return output_json


app = Flask(__name__)

# /weather?city=$City&country=$Country
@app.route('/weather', methods =['GET'])
def weather():
    """Main function of Weather API."""
    
    app.config.from_pyfile('settings.py')
    app.wsgi_app = LoggerMiddleware(app.wsgi_app)
    app.config['JSON_SORT_KEYS'] = False

    # Initial validators
    check_file('.env')

    # Check main args: city and country
    city  = request.args.get('city', None)
    country  = request.args.get('country', None)
    check_city(city)
    check_country(country)

    # Args transformation
    city = str(city).replace(' ', '%20')
    country = str(country)

    # Load env variables
    api_url = app.config.get("API_URL")
    api_key = app.config.get("API_KEY")


    # Core functions
    city_country = f"{city},{country}"
    owmap_response = openweathermap_api(api_url, api_key, city_country)
    input_json = json.loads(owmap_response)
    
    output_json = create_response_body(input_json)
    return jsonify(output_json)


if __name__ == '__main__':
    app.run()
