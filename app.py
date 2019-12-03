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
        return "item already exists"
    else:
        items.add(item)
        return "pass"

@app.route('/delete/', methods=['GET'])
def delete():
    item = request.args.get('item')

    if(item in items):
        items.remove(item)
        return "pass"
    else:
        return "item does not exist"

@app.route('/update/', methods=['PUT'])
def update():
    request_dict = request.args.to_dict()
#    print(request_dict, file=sys.stderr)

    


#    olditem = request.args.get('old-item', None)
#    repacementitem = request.args.get('replacement-item', None)
    
    if(('old-item' in request_dict) and ('replacement-item' in request_dict)):
        if(request_dict['old-item'] in items):
            items.remove(request_dict['old-item'])
            items.add(request_dict['replacement-item']) 
            return "successfully updated"
        else:
            return "old-item does not exist"
    else:
        return "old-item and replacement-item values required"

@app.route('/read/', methods=['GET'])
def read():
    item = request.args.get('item')
    
    if(item in items):
        return "item: " + item + " exists in storage"
    else:
        return "item does not exist"


if (__name__ == '__main__'):
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)

