# -*- coding: utf-8 -*-
"""Functions to check (env) variables and route args for My Weather API."""

import re
import logging
from flask import abort

def check_emptiness(var_name, var_val, reg_expr=None):
    """Verify if a variable is None/empty."""
    if var_val is None:
        logging.error(f" {var_name} is '{var_val}'.")
        abort(500)
    if var_val == '':
        logging.error(f" {var_name} is '{var_val}' (empty).")
        abort(500)
    logging.debug(f" {var_name}='{var_val}' was loaded: OK")


def check_regex(arg_name, arg, reg_expr):
    """Verify if an arg matches with a specific regex."""
    arg_str = str(arg)
    pattern = re.compile(reg_expr)
    if pattern.fullmatch(arg_str) is None:
        logging.error(f" {arg_name}:'{arg_str}' doesn't match with '{reg_expr}' regex")
        abort(400)
    else:
        logging.debug(f" {arg_name}:'{arg_str}' matchs with '{reg_expr}' regex: OK")



