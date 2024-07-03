#!/usr/bin/env python3
"""
This module forces a particular locale by passing the locale=fr parameter
"""

from flask import Flask, render_template, request
from flask_babel import Babel 


class Config:
    """
    This class contains langauges and timezone
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Check if locale parameter is in the request args
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_language.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    basic route
    """
    return render_template('4-index.html',
                           home_title=_('Welcome to Holberton'),
                           home_header=_('Hello world!'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
