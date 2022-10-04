from flask import Flask, Blueprint
import urllib3
import json

from config import config
from src.services.RecorderManager import RecorderManager
from src.delivery.routes.api import rec, relays, sting, system, window_openers

http = urllib3.PoolManager()
api = Blueprint('api', __name__)


recorder_manager = RecorderManager()


@api.route('/', methods=["GET"])
def root():
    return "Api is on"


api.register_blueprint(rec.rec, '/rec')
api.register_blueprint(relays.relays, '/relays')
api.register_blueprint(sting.sting, '/sting')
api.register_blueprint(system.system, '/system')
api.register_blueprint(window_openers.window_openers, '/window_openers')
