from src.messaging.Consumer import Consumer


class StingFaceDetectionConsumer(Consumer):
    def __init__(self):
        super().__init__(['Sting'])

    def process(self, message):
        pass
