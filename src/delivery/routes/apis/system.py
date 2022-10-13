from flask import Flask, Blueprint
import urllib3
import os

from config import config

http = urllib3.PoolManager()
system = Blueprint('system', __name__)


@system.route('/sting/reboot/', methods=["GET"])
def reboot_sting():
    url = config['apis']['sting'] + 'restart/'
    http.request('GET', url)

    return {"status": "Sting was rebooted"}, 200


@system.route('/detector/restart/', methods=["GET"])
def restart_detector():
    res = os.system('sudo service detector restart')
    print(res)

    return {"status": "Detector was restarted"}, 200


@system.route('/detector/stop/', methods=["GET"])
def stop_detector():
    res = os.system('sudo service detector stop')
    print(res)

    return {"status": "Detector was stopped"}, 200


@system.route('/detector/start/', methods=["GET"])
def start_detector():
    res = os.system('sudo service detector start')
    print(res)

    return {"status": "Detector was started"}, 200


@system.route('/detector/status/', methods=["GET"])
def detector_status():
    res = os.system('sudo service detector status')
    print(res)

    return {"status": "Sting was rebooted"}, 200
