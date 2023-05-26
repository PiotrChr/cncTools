from src.messaging.Producer import Producer


class StingHumanDetectionProducer(Producer):
    def __init__(self):
        super().__init__('StingObjectDetections')

    def produce(self, frame):
        self.send('detected_object_frame', frame)
