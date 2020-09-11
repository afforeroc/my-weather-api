# -*- coding: utf-8 -*-
"""Load API settings of OpenWeather API."""

from os import environ

API_URL = environ.get('API_URL')
API_KEY = environ.get('API_KEY')
