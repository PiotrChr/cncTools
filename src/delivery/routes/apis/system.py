from flask import Flask, Blueprint
import urllib3
import os
import subprocess
import re

from config import config

http = urllib3.PoolManager()
system = Blueprint('system', __name__)

detector_status_pattern = re.compile(r'Active:.([a-z]*)', flags=re.MULTILINE)


@system.route('/sting/reboot/', methods=["GET"])
def reboot_sting():
    url = config['apis']['sting'] + 'restart/'
    http.request('GET', url)

    return {"status": "Sting was rebooted"}, 200


@system.route('/detector/restart/', methods=["GET"])
def restart_detector():
    res = subprocess.run(
        ['sudo', 'systemctl', 'restart', 'detector.service'],
        stdout=subprocess.PIPE
    ).stdout.decode('utf-8')

    print(res)

    return {"status": "Detector was restarted"}, 200


@system.route('/detector/stop/', methods=["GET"])
def stop_detector():
    res = subprocess.run(
        ['sudo', 'systemctl', 'stop', 'detector.service'],
        stdout=subprocess.PIPE
    ).stdout.decode('utf-8')

    print(res)

    return {"status": "Detector was stopped"}, 200


@system.route('/detector/start/', methods=["GET"])
def start_detector():
    res = subprocess.run(
        ['sudo', 'systemctl', 'start', 'detector.service'],
        stdout=subprocess.PIPE
    ).stdout.decode('utf-8')

    print(res)

    return {"status": "Detector was started"}, 200


@system.route('/detector/status/', methods=["GET"])
def detector_status():
    res = subprocess.run(
        ['sudo', 'systemctl', 'status', 'detector.service'],
        stdout=subprocess.PIPE
    ).stdout.decode('utf-8')

    status = detector_status_pattern.search(res)

    if status is None:
        return {"status": "Error reading status"}, 500

    return {"data": {"status": status[1], "full_status": res}}, 200
