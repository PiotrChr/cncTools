from flask import Flask, Blueprint
import urllib3
import json

from config import config
from src.services.RecorderManager import RecorderManager
from src.delivery.routes.apis import rec, relays, sting, system, window_openers, notifications

http = urllib3.PoolManager()
api = Blueprint('api', __name__)


recorder_manager = RecorderManager()


@api.route('/', methods=["GET"])
def root():
    return "Api is on"


api.register_blueprint(rec.rec, url_prefix='/rec')
api.register_blueprint(relays.relays, url_prefix='/relays')
api.register_blueprint(sting.sting, url_prefix='/sting')
api.register_blueprint(system.system, url_prefix='/system')
api.register_blueprint(window_openers.window_openers, url_prefix='/window_openers')
api.register_blueprint(notifications.notifications, url_prefix='/notifications')
