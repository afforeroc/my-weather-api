# -*- coding: utf-8 -*-
"""Required middleware to monitoring logs and errors."""

from flask import Request


class Middleware:
    """Middleware class that prints the path and the URL request."""
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # not Flask request - from werkzeug.wrappers import Request
        request = Request(environ)
        print('--> PATH: %s, URL: %s' % (request.path, request.url))
        # just do here everything what you need
        return self.app(environ, start_response)
