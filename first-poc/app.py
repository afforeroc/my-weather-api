# -*- coding: utf-8 -*-
"""Create a Weather API using a framework if you like."""
import os
import json
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
    json_data = urllib.request.urlopen(api_url + city + '&appid=' +
                                       api_key).read()
    return json_data


def beautiful_json(data_json):
    """Print in console a JSON data in beautiful style."""
    json_data = json.dumps(data_json, indent=2,
                           ensure_ascii=False).encode('utf8')
    print(json_data.decode())


app = Flask(__name__)
api_url, api_key = load_env_owmap('.env')

@app.route('/')
def example():
    """Return a sample JSON response."""
    #owmap_response = openweathermap_api(api_url, api_key, 'Bogota')
    #json_data = json.loads(owmap_response)
    #beautiful_json(json_data)
    return '{"name":"Bob"}'


if __name__ == '__main__':
    app.run()
