import flask
from flask import Flask, render_template, request
import re
import sys
import os


#init flask app
app = Flask(__name__)


@app.route('/')
def home_endpoint():
    return 'Hello World!'


if (__name__ == '__main__'):
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)

