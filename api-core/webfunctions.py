# -*- coding: utf-8 -*-
"""Functions to manipulate JSON and datetime objects for My Weather API."""

from datetime import datetime
import calendar
import json
from flask import make_response, jsonify, abort


def get_place(city, country):
    """Join city and country args."""
    city = str(city).replace(' ', '%20')
    country = str(country)
    return f"{city},{country}"


def reply_bad_response(input_json):
    """ The bad response will be same that it was obtained from OpenWeatherMap."""
    if str(input_json['cod']) != '200':
        code = int(input_json['cod'])
        message = str(input_json['message'])
        bad_response = make_response(jsonify(message=message), code)
        abort(bad_response)


def get_datetime_from_unix(now, input_json=None, arg=None):
    """Return current datetime from the current unix timestamp."""
    if now:
        datetime_utc = datetime.utcnow()
        datetime_ut = calendar.timegm(datetime_utc.utctimetuple())
    else:
        datetime_ut = input_json[arg]
    datetime_ts = datetime.fromtimestamp(datetime_ut)
    requested_datetime = datetime_ts.strftime('%Y-%m-%d %H:%M:%S')
    return requested_datetime


# Debug function to see data_json in console.
def beautiful_json(data_json):
    """Print in console a JSON data in beautiful style."""
    json_data = json.dumps(data_json,
                           indent=4,
                           ensure_ascii=False,
                           sort_keys=False).encode('utf8')
    print(json_data.decode())


def get_val_unit(json_data, arg1, arg2, unit):
    """Extract value from JSON and concatenate with a unit."""
    value = str(json_data[arg1][arg2])
    return f"{value}{unit}"


def get_cloudines(input_json):
    """Return the cloudiness using a phrase description."""
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


def get_hour_time(input_json, arg1, arg2):
    """Return a specific HH:MM from a unix time provided."""
    datetime_unix = int(input_json[arg1][arg2])
    datetime_ts = datetime.fromtimestamp(datetime_unix)
    return datetime_ts.strftime('%H:%M')


def create_response_body(input_json):
    """Create a json response with specific args of input JSON."""
    city_name = str(input_json['name'])
    country_code = str(input_json['sys']['country'])
    temp_celsius = get_val_unit(input_json, 'main', 'temp', ' °C')
    wind_speed = get_val_unit(input_json, 'wind', 'speed', ' m/s')
    wind_deg = get_val_unit(input_json, 'wind', 'deg', ' deg')
    cloudines = get_cloudines(input_json)
    pressure = get_val_unit(input_json, 'main', 'pressure', ' hPa')
    humidity_percent = get_val_unit(input_json, 'main', 'humidity', '%')
    coord_lon = str(input_json['coord']['lon'])
    coord_lat = str(input_json['coord']['lat'])
    sunrise_hour = get_hour_time(input_json, 'sys', 'sunrise')
    sunset_hour = get_hour_time(input_json, 'sys', 'sunset')
    requested_time = get_datetime_from_unix(0, input_json, 'dt')

    output_json = {
        "location_name": f"{city_name}, {country_code}",
        "temperature": temp_celsius,
        "wind": f"{wind_speed}, {wind_deg}",
        "cloudines": cloudines,
        "pressure": pressure,
        "humidity": humidity_percent,
        "sunrise": sunrise_hour,
        "sunset": sunset_hour,
        "geo_coordinates": [coord_lat, coord_lon],
        "requested_time": requested_time
    }
    return output_json
