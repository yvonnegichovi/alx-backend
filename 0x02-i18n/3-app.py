#!/usr/bin/env python3
"""
This module Use the _ or gettext function to parametrize your templates
"""

from flask import Flask, render_template
from flask_babel import Babel, gettex as _

app = Flask(__name__)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
