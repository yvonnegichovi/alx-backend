#!/usr/bin/env python3
"""
This module uses Babel to create function get_locale
"""

from flask import Flask, g, request, render_template
from flask_babel import Babel


app = Flask(__name__)


babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determines the best match with the supported languages
    """
    return request.accept_languages.best_match(['fr', 'en'])
