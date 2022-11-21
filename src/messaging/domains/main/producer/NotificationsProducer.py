import json
from datetime import datetime
from src.messaging.Producer import Producer

STING_NOTIFICATION = 'sting_notification'


class NotificationsProducer(Producer):
    def __init__(self):
        super().__init__('Notifications')

    def produce(
        self,
        key='default_notification',
        short='Notification description',
        full=None
    ):
        if full is None:
            full = short

        message_value = json.dumps({
            'date': (datetime.now()).isoformat(),
            'message': {
                'short': short,
                'full': full
            }
        })

        self.send(key, message_value)
