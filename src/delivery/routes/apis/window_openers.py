from flask import Flask, Blueprint
import urllib3

from config import config

http = urllib3.PoolManager()

window_openers = Blueprint('window_openers', __name__)


@window_openers.route('/<string:window_opener_name>/open', methods=['GET'])
def open_window(window_opener_name: str):
    opener = config['window_openers'][window_opener_name]
    req = http.request('GET', opener['source'] + '/full_open')

    return {"data": {"status": "Window opened"}}, 200


@window_openers.route('/<string:window_opener_name>/close', methods=['GET'])
def close_window(window_opener_name: str):
    opener = config['window_openers'][window_opener_name]
    req = http.request('GET', opener['source'] + '/full_close')

    return {"data": {"status": "Window closed"}}, 200


@window_openers.route('/<string:window_opener_name>/step_up', methods=['GET'])
def window_step_up(window_opener_name: str):
    opener = config['window_openers'][window_opener_name]
    req = http.request('GET', opener['source'] + '/step_up')

    return {"data": {"status": "Window stepped up"}}, 200


@window_openers.route('/<string:window_opener_name>/step_down', methods=['GET'])
def window_step_down(window_opener_name: str):
    opener = config['window_openers'][window_opener_name]
    req = http.request('GET', opener['source'] + '/step_down')

    return {"data": {"status": "Window stepped down"}}, 200


@window_openers.route('/<string:window_opener_name>/open_to/<int:open_value>', methods=['GET'])
def window_open_to(window_opener_name: str, open_value: int):
    opener = config['window_openers'][window_opener_name]
    url = opener['source'] + '/open?p=' + open_value
    req = http.request('GET', url)

    return {"data": {"status": "Window opened to: " + str(open_value)}}, 200
