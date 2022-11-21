from flask import Flask, Blueprint
import json
from config import config
from src.messaging.domains.main.consumer.StingNotificationsConsumer import StingNotificationsConsumer

notifications = Blueprint('main', __name__)

stingNotificationsConsumer = StingNotificationsConsumer()
stingNotificationsConsumer.subscribe()


@notifications.route('/sting_detections/', methods=["GET"])
def sting_detections():
    messages = stingNotificationsConsumer.consume_all(num_messages=10)

    return {"data": {"notifications": messages}}
