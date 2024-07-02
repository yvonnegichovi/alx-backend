#!/usr/bin/env python3
"""
This module uses Babel to create function get_locale
"""

from flask import Flask, g, request, render_template
from flask_babel import Babel


app = Flask(__name__)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determines the best match with the supported languages
    """
    return request.accept_languages.best_match(['fr', 'en'])

@app.route('/')
def index():
    """
    The home/index page.
    """
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(debug=True)
