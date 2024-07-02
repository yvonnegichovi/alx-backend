#!/usr/bin/env python3
"""
This module infers appropriate time zone
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """
    Gets the user
    """
    return users.get(user_id)

@babel.timezoneselector
def get_timezone():
    """
    Checks URL parameters
    """
    tz_param = request.args.get('timezone')
    if tz_param:
        try:
            pytz.timezone(tz_param)
            return tz_param
        except pytz.UnknownTimeZoneError:
            pass
    user = getattr(g, 'user', None)
    if user and user['timezone']:
        try:
            pytz.timezone(user['timezone'])
            return user['timezone']
        except pytz.UnknownTimeZoneError:
            pass
    return 'UTC'

@app.before_request
def before_request():
    """
    Finds a user if any, and set it as a global on flask.g.user
    """
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None

@app.route('/')
def index():
    """
    The home/index page.
    """
    user = g.user
    return render_template('7-index.html', user=user)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
