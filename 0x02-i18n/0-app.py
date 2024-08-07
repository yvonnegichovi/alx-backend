#!/usr/bin/env python3
"""
This module is a Flask app where APIs will be created
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    basic route that renders a template
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
