from src.messaging.Producer import Producer


class StingHumanRecognizedProducer(Producer):
    def __init__(self):
        super().__init__(['Sting'])

    def produce(self):
        pass
