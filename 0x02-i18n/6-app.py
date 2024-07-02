#!/usr/bin/env python3
"""
This module creates a user login system outside the scope o the project
"""

from flask import Flask, g, render_template, request


app = Flask(__name__)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

supported_locales = ['en', 'fr']

def get_locale():
    """
    Check locale from URL parameters
    """
    locale = request.args.get('locale')
    if locale in supported_locales:
        return locale
    if g.user and g.user.get('locale') in supported_locales:
        return g.user['locale']
    header_locale = request.headers.get('Accept-Language')
    if header_locale:
        header_locale = header_locale.split(',')[0][:2]
        if header_locale in supported_locales:
            return header_locale
    return 'en'


@app.before_request
def before_request():
    """
    Finds a user if any, and set it as a global on flask.g.user
    """
    g.user = get_user()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
