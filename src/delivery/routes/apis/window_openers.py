from flask import Flask, Blueprint
import urllib3
import json

from config import config

http = urllib3.PoolManager()

window_openers = Blueprint('window_openers', __name__)

def get_opener_by_id(opener_id: int):
    for opener in config['window_openers']:
        if opener_id == opener['id']:
            return opener
    
    return None


@window_openers.route('/<int:opener_id>/open/', methods=['GET'])
def open_window(opener_id: int):
    opener = get_opener_by_id(opener_id)
    req = http.request('GET', opener['source'] + '/full_open')

    return {"data": {"status": "Window opened"}}, 200


@window_openers.route('/<int:opener_id>/close', methods=['GET'])
def close_window(opener_id: int):
    opener = get_opener_by_id(opener_id)
    req = http.request('GET', opener['source'] + '/full_close')

    return {"data": {"status": "Window closed"}}, 200


@window_openers.route('/<int:opener_id>/step_up/', methods=['GET'])
def window_step_up(opener_id: int):
    opener = get_opener_by_id(opener_id)
    req = http.request('GET', opener['source'] + '/step_up')

    return {"data": {"status": "Window stepped up"}}, 200


@window_openers.route('/<int:opener_id>/step_down/', methods=['GET'])
def window_step_down(opener_id: int):
    opener = get_opener_by_id(opener_id)
    req = http.request('GET', opener['source'] + '/step_down')

    return {"data": {"status": "Window stepped down"}}, 200


@window_openers.route('/<int:opener_id>/open_to/<int:open_value>/', methods=['GET'])
def window_open_to(opener_id: int, open_value: int):
    opener = get_opener_by_id(opener_id)
    url = opener['source'] + '/open?p=' + open_value
    req = http.request('GET', url)

    return {"data": {"status": "Window opened to: " + str(open_value)}}, 200


@window_openers.route('/<int:opener_id>/status/', methods=['GET'])
def window_status(opener_id: int):
    opener = get_opener_by_id(opener_id)
    url = opener['source'] + '/status'
    req = http.request('GET', url)
    
    data = json.loads(req.data.decode('utf-8'))

    return {"data": data}, 200
