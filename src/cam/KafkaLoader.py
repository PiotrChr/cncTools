from src.cam.Loader import Loader
from src.messaging.domains.sting.consumer.FrameConsumer import FrameConsumer
import cv2


class KafkaLoader(Loader):
    def __init__(self, topics, conf):
        self.FConsumer = FrameConsumer(topics, conf)
        super().__init__(0.00, topics[0])

    def get_frame(self):
        return self.FConsumer.consume(False)

    def start_read(self):
        self.FConsumer.subscribe()
        print("Stream for:" + str(self.camera_id) + " started, writing to buffer")
        self.read()

    def cleanup(self):
        self.FConsumer.close()

    def prepare_output_frame(self, frame):
        ret, buffer = cv2.imencode('.jpg', frame)
        output = buffer.tobytes()

        return output
