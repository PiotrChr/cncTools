from src.messaging.Producer import Producer


class StingFaceDetectionProducer(Producer):
    def __init__(self):
        super().__init__(['StingFaceDetections'])

    def produce(self, frame):
        self.send('detected_face_frame', frame)
