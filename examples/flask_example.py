# -*- coding: utf-8 -*-
from flask import Flask, request, abort
from apiexplorer.flask import add_explorer_to
import time
from datetime import datetime

app = Flask(__name__)
add_explorer_to(app)

cache = {}

def generate_new_id():
    return str(int(time.mktime(datetime.utcnow().timetuple())))

@app.route('/cache', methods=['POST'])
def create():
    '''Create a new cached item.
    '''
    item_id = generate_new_id()
    cache[item_id] = request.data
    return item_id

@app.route('/cache/<string:item_id>', methods=['GET'])
def read(item_id):
    '''Read a cached item.
    '''
    if item_id not in cache:
        abort(404)

    return cache[item_id]

@app.route('/cache/<string:item_id>', methods=['PUT'])
def update(item_id):
    '''Update or create a cached item.
    '''
    if item_id in cache:
        status = 204
    else:
        status = 201

    cache[item_id] = request.data

    return '', status

@app.route('/cache/<string:item_id>', methods=['DELETE'])
def delete(item_id):
    '''Delete a cached item.
    '''
    if item_id not in cache:
        abort(404)

    item = cache[item_id]
    del cache[item_id]

    return item


if __name__ == '__main__':
    app.run(debug=True)
