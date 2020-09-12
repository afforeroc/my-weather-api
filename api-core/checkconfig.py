# -*- coding: utf-8 -*-
"""Functions to check config files of My weather API."""

import os
from flask import abort
import logging

logging.basicConfig(level=logging.DEBUG)

def check_file(pathfile):
    """Check if a pathfile exists and is not empty."""
    if not os.path.isfile(pathfile) or os.stat(pathfile).st_size == 0:
        return 0
    else:
        return 1