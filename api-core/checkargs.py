# -*- coding: utf-8 -*-
"""Functions to check the route args of My weather API."""

import re
from flask import abort


def check_empty(arg_name, arg):
    """Check if a arg isn't empty."""
    if arg is None or arg == '':
        print(f">> EXTERNAL ERROR! '{arg_name}' arg is empty")
        abort(400)
    else:
        print(f"OK: '{arg_name}' arg is not empty")


def check_arg(arg_name, arg, reg_expr, message):
    """Check if 'city' arg is a string composed only by with letters."""
    arg_str = str(arg)
    #reg_expr = "[A-Za-z ]+"  # String composed only by with letters
    pattern = re.compile(reg_expr)
    if pattern.fullmatch(arg_str) is None:
        print(f">> EXTERNAL ERROR! {arg_name}:'{arg_str}' isn't a {message}")
        abort(400)
    else:
        print(f"OK: {arg_name}:'{arg_str}' is a {message}")
