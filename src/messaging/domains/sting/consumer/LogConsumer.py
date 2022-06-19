from src.messaging.Consumer import Consumer


class LogConsumer(Consumer):
    def __init__(self):
        super().__init__(['Sting'])

    def process(self, message):
        pass
