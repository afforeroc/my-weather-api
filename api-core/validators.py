# -*- coding: utf-8 -*-
"""Functions to check (env) variables and route args for My Weather API."""

import re
import logging
from flask import abort


def check_emptiness(var_name, var_val):
    """Verify if a variable is None/empty."""
    if var_val is None:
        error_message = f" {var_name} is '{var_val}'."
        logging.error(error_message)
        abort(500)
    if var_val == '':
        error_message = f" {var_name} is '{var_val}' (empty)."
        logging.error(error_message)
        abort(500)
    sucess_message = f" {var_name}='{var_val}' was loaded: OK"
    logging.debug(sucess_message)


def check_regex(var_name, var, reg_expr):
    """Verify if an var matches with a specific regex."""
    var_str = str(var)
    pattern = re.compile(reg_expr)
    if pattern.fullmatch(var_str) is None:
        error_message = f" {var_name}:'{var_str}' doesn't match with '{reg_expr}' regex"
        logging.error(error_message)
        abort(400)
    else:
        sucess_message = f" {var_name}='{var}' matches with '{reg_expr}' regex: OK"
        logging.debug(sucess_message)
