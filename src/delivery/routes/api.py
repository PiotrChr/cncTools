from flask import Flask, Blueprint
import urllib3
import json

from config import config
from src.services.RecorderManager import RecorderManager

http = urllib3.PoolManager()
api = Blueprint('api', __name__)


recorder_manager = RecorderManager()


@api.route('/', methods=["GET"])
def root():
    return "Api is on"


@api.route('/rec/delete/', methods=["DELETE"])
def delete_rec():
    pass


@api.route('/rec/status', methods=["GET"])
def recording_status():
    rec_status, recordings = recorder_manager.get_rec_status()

    return {"recordings": recordings, "status": rec_status}, 200


@api.route('/rec/stop/<int:camera>', methods=["GET"])
def stop_record(camera: int):
    if not recorder_manager.stop_record(camera):
        return {"data": {"error": "Camera not recording"}}, 400

    return {"data": {"status": "Camera stopped recording"}}, 201


@api.route('/rec/start/<int:camera>', methods=["GET"])
def start_record(camera: int):
    if not recorder_manager.start_record(camera):
        return {"data": {"error": "Camera" + "already recording"}}, 400

    return {"data": {"status": "Camera started recording"}}, 200


@api.route('/rec/delete/<int:camera>/<string:recording>', methods=["GET"])
def delete_record(camera: int, recording: str):
    recorder_manager.delete_record(camera, recording)

    return {"data": {"status": "Camera recording removed"}}, 200


@api.route('/window_openers/<string:window_opener_name>/open', methods=['GET'])
def open_window(window_opener_name: str):
    opener = config['window_openers'][window_opener_name]
    req = http.request('GET', opener['source'] + '/full_open')

    return {"data": {"status": "Window opened"}}, 200


@api.route('/window_openers/<string:window_opener_name>/close', methods=['GET'])
def close_window(window_opener_name: str):
    opener = config['window_openers'][window_opener_name]
    req = http.request('GET', opener['source'] + '/full_close')

    return {"data": {"status": "Window closed"}}, 200


@api.route('/window_openers/<string:window_opener_name>/step_up', methods=['GET'])
def window_step_up(window_opener_name: str):
    opener = config['window_openers'][window_opener_name]
    req = http.request('GET', opener['source'] + '/step_up')

    return {"data": {"status": "Window stepped up"}}, 200


@api.route('/window_openers/<string:window_opener_name>/step_down', methods=['GET'])
def window_step_down(window_opener_name: str):
    opener = config['window_openers'][window_opener_name]
    req = http.request('GET', opener['source'] + '/step_down')

    return {"data": {"status": "Window stepped down"}}, 200


@api.route('/window_openers/<string:window_opener_name>/open_to/<int:open_value>', methods=['GET'])
def window_open_to(window_opener_name: str, open_value: int):
    opener = config['window_openers'][window_opener_name]
    url = opener['source'] + '/open?p=' + open_value
    req = http.request('GET', url)

    return {"data": {"status": "Window opened to: " + str(open_value)}}, 200


@api.route('/relay/status', methods=['GET'])
def relay_status():
    status_request = http.request('GET', config['relays']['status_url'])
    data = json.loads(status_request.data.decode('utf-8'))

    return {"data": {"status": data}}, 200


@api.route('/relays/on/<int:relay>', methods=["GET"])
def relay_on(relay):
    on_request = http.request('GET', config['relays']['on_url'], fields={"r": relay})

    return {"data": {"status": "Ok"}}, 200


@api.route('/relays/off/<int:relay>', methods=["GET"])
def relay_off(relay):
    off_request = http.request('GET', config['relays']['off_url'], fields={"r": relay})

    return {"data": {"status": "Ok"}}, 200
