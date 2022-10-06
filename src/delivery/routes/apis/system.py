from flask import Flask, Blueprint
import urllib3

from config import config

http = urllib3.PoolManager()
system = Blueprint('system', __name__)


@system.route('/sting/reboot/', methods=["GET"])
def reboot_sting():
    url = config['apis']['sting'] + 'restart/'
    http.request('GET', url)

    return {"status": "Sting was rebooted"}, 200
