# -*- coding: utf-8 -*-
"""Functions to check config files of My weather API."""

import os
from flask import abort


def check_file(pathfile):
    """Check if a pathfile exists and is not empty."""
    if not os.path.isfile(pathfile):
        print(f">> INTERNAL ERROR! '{pathfile}' file was not found")
        abort(500)
    elif os.stat(pathfile).st_size == 0:
        print(f">> INTERNAL ERROR! '{pathfile}' file is empty")
        abort(500)
    else:
        print(f"OK: '{pathfile}' file exits and is not empty")
