#!/usr/bin/python3
'''A simple Flask web application.
'''
from flask import Flask


app = Flask(__name__)
'''The Flask application instance.'''


@app.route('/', strict_slashes=False)
def index():
    '''The home page.'''
    return 'Hello HBNB!\n'


if __name__ == '__main__':
    app.run('0.0.0.0', '5000')
