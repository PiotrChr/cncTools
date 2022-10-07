from flask import Flask, Blueprint
import urllib3
import json

from config import config

http = urllib3.PoolManager()
relays = Blueprint('relays', __name__)


@relays.route('/status', methods=['GET'])
def relay_status():
    status_request = http.request('GET', config['relays']['status_url'])
    data = json.loads(status_request.data.decode('utf-8'))

    return {"data": {"status": data}}, 200


@relays.route('/on/<int:relay>', methods=["GET"])
def relay_on(relay):
    on_request = http.request(
        'GET', config['relays']['on_url'], fields={"r": relay})

    return {"data": {"status": "Ok"}}, 200


@relays.route('/off/<int:relay>', methods=["GET"])
def relay_off(relay):
    off_request = http.request(
        'GET', config['relays']['off_url'], fields={"r": relay})

    return {"data": {"status": "Ok"}}, 200
