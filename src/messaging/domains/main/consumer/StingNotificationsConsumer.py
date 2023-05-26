from src.messaging.Consumer import Consumer
from config import config
import json

STING_NOTIFICATIONS_KEY = 'sting_notification'


class StingNotificationsConsumer(Consumer):
    def __init__(self, topics=None, conf=config["kafka"]["notifications_consumer_conf"]):
        if topics is None:
            topics = ['Notifications']

        super().__init__(topics, conf)

    def process(self, msg):
        if msg.key().decode("utf-8") == STING_NOTIFICATIONS_KEY:
            return json.loads(msg.value().decode("utf-8"))

