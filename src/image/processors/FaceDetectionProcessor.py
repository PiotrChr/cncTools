from src.image.processors.Processor import Processor
from src.image.FaceDetector import FaceDetector
from src.messaging.domains.sting.producer.StingFaceDetectionProducer import StingFaceDetectionProducer
import cv2
import imutils


class FaceDetectionProcessor(Processor):
    def __init__(self, frame_skip=0, daemon=False):
        super().__init__(self.__class__.__name__, frame_skip)
        self.daemon = daemon

        self.restart = False
        self.face_detector = FaceDetector()

        self.last_recognition_id = None
        self.FDProducer = StingFaceDetectionProducer()

    def on_recognition(self, frame, label, recognition_id):
        if recognition_id != self.last_recognition_id:
            self.last_recognition_id = recognition_id

            if frame is not None:
                byte_image = cv2.imencode('.jpg', frame)[1].tostring()
                self.FDProducer.produce(byte_image)

    def process(self, frame):
        if not self.should_process():
            return None

        if self.restart:
            self.restart = False

        frame = imutils.resize(frame, width=300)
        frame = cv2.rotate(frame, cv2.cv2.ROTATE_180)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if self.daemon:
            self.face_detector.run(frame)
        else:
            frame = self.face_detector.detect(frame)

        self.yield_val = ()

        return frame
