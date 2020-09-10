# -*- coding: utf-8 -*-
"""Create a Weather API using a framework if you like."""
import os
import json
import datetime
import urllib.request
from dotenv import load_dotenv
from flask import Flask


def load_env_owmap(env_file):
    """Load auth settings for OpenWeatherMap."""
    dotenv_path = os.path.join(os.path.dirname(__file__), env_file)
    load_dotenv(dotenv_path)
    api_url = os.getenv('api_url')
    api_key = os.getenv('api_key')
    return api_url, api_key


def openweathermap_api(api_url, api_key, city=None):
    """Request weather data from OpenWeatherMap."""
    # source contain json data from api
    json_data = urllib.request.urlopen(api_url + city + '&units=metric&appid=' +
                                       api_key).read()
    return json_data


def beautiful_json(data_json):
    """Print in console a JSON data in beautiful style."""
    json_data = json.dumps(data_json, indent=2,
                           ensure_ascii=False).encode('utf8')
    print(json_data.decode())


def get_location_name(input_json):
    """..."""
    city = str(input_json['name'])
    country_code = str(input_json['sys']['country'])
    location_name = f"{city}, {country_code}"
    return location_name


def get_temperature(input_json):
    """..."""
    celsius_deg = str(input_json['main']['temp'])
    return f"{celsius_deg} °C"


def get_wind(input_json):
    """..."""
    wind_speed = float(input_json['wind']['speed'])
    wind_deg = int(input_json['wind']['deg'])
    wind_deg = int(input_json['wind']['deg'])
    wind = f"{wind_speed} m/s, {wind_deg} deg"
    return wind


def get_humidity(input_json):
    """..."""
    humidity_val = str(input_json['main']['humidity'])
    humidity = f"{humidity_val}%"
    return humidity


def get_pressure(input_json):
    """..."""
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

    json_response = {
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
    output_json = json.dumps(json_response, indent=4, sort_keys=False)
    return output_json


app = Flask(__name__)

@app.route('/')
def example():
    """Return a sample JSON response."""
    api_url, api_key = load_env_owmap('.env')
    owmap_response = openweathermap_api(api_url, api_key, 'Bogota')
    input_json = json.loads(owmap_response)
    beautiful_json(input_json)
    print(json.dumps(input_json, indent=4, sort_keys=False))
    output_json = create_response_body(input_json)
    return output_json


if __name__ == '__main__':
    app.run()
