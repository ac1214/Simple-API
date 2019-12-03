import flask
from flask import Flask, render_template, request
import re
import sys
import os


#init flask app
app = Flask(__name__)

items = set()

@app.route('/')
def home_endpoint():
    return 'Hello World!'

@app.route('/create/', methods=['PUT'])
def create():
    item = request.args.get('item')
    print("testing item: " + item, file=sys.stderr)

    if(item in items):
        return "item already exists"
    else:
        items.add(item)
        return "pass"

@app.route('/delete/', methods=['GET'])
def delete():
    item = request.args.get('item')
    print("testing item: " + item, file=sys.stderr)

    if(item in items):
        items.remove(item)
        return "pass"
    else:
        return "item does not exist"



if (__name__ == '__main__'):
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)

