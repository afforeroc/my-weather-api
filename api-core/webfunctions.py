# -*- coding: utf-8 -*-
"""Functions to manipulate JSON objects of My weather API."""

import datetime
import json
from random import randint
import urllib.request


def get_random_num():
    rand_num = randint(1, 100)
    output_json = { "number": rand_num}
    return output_json

def get_place(city, country):
    """Join city and country args."""
    city = str(city).replace(' ', '%20')
    country = str(country)
    return f"{city},{country}"


def request_ow_api(api_url, api_key, city_country):
    """Request weather data from OpenWeather API."""
    request_api = str(api_url) + str(
        city_country) + '&units=metric&appid=' + str(api_key)
    json_data = urllib.request.urlopen(request_api).read()
    return json_data


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
    datetime_ts = datetime.datetime.fromtimestamp(datetime_unix)
    return datetime_ts.strftime('%H:%M')


def get_requested_time(input_json, arg1):
    """Return full date time of call request."""
    requested_ut = int(input_json[arg1])
    requested_ts = datetime.datetime.fromtimestamp(requested_ut)
    requested_time = requested_ts.strftime('%Y-%m-%d %H:%M:%S')
    return requested_time


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
    requested_time = get_requested_time(input_json, 'dt')

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
