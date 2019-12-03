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

    if(item in items):
        return "item already exists", 304
    else:
        items.add(item)
        return "pass", 201

@app.route('/delete/', methods=['GET'])
def delete():
    item = request.args.get('item')

    if(item in items):
        items.remove(item)
        return "pass", 200
    else:
        return "item does not exist", 404

@app.route('/update/', methods=['PUT'])
def update():
    request_dict = request.args.to_dict()
    
    if(('old-item' in request_dict) and ('replacement-item' in request_dict)):
        if(request_dict['old-item'] in items):
            items.remove(request_dict['old-item'])
            items.add(request_dict['replacement-item']) 
            return "successfully updated", 202
        else:
            return "old-item does not exist", 404
    else:
        return "old-item and replacement-item values required", 206

@app.route('/read/', methods=['GET'])
def read():
    item = request.args.get('item')
    
    if(item in items):
        return "item: " + item + " exists in storage", 200
    else:
        return "item does not exist", 404


if (__name__ == '__main__'):
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)

