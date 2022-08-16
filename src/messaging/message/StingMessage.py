from src.messaging.message.Message import Message


class StingMessage(Message):
    def __init__(self, message_name="default"):
        self.message_name = message_name

    def to_json(self):
        pass
