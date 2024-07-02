#!/usr/bin/env python3
"""
This module infers appropriate time zone
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime, gettext
import pytz
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    """
    Gets the user
    """
    return users.get(user_id)

@babel.timezoneselector
def get_timezone() -> str:
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

    if g.user:
        user_timezone = g.user.get('timezone')
        if user_timezone:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except pytz.UnknownTimeZoneError:
                pass

    return 'UTC'

@app.before_request
def before_request():
    """
    Finds a user if any, and set it as a global on flask.g.user
    """
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None

@app.route('/')
def index():
    """Get current time in the inferred time zone"""
    current_time = format_datetime(datetime.utcnow(), format='medium', timezone=get_timezone())

    if g.user:
        message = gettext("The current time is %(current_time)s.", current_time=current_time)
    else:
        message = gettext("You are not logged in.")

    return render_template('index.html', message=message, current_time=current_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
