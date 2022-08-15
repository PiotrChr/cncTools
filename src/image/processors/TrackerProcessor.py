from src.image.processors.Processor import Processor
from src.image.ObjectTracker import ObjectTracker
from src.messaging.domains.sting.producer.StingHumanDetectionProducer import StingHumanDetectionProducer
from src.robot_controller.RobotController import RobotController
import cv2
import imutils


class TrackerProcessor(Processor):
    def __init__(self, frame_skip=0, daemon=False):
        super().__init__(self.__class__.__name__, frame_skip)
        self.robot_controller = RobotController()
        self.daemon = daemon
        self.restart = False
        self.tracker = ObjectTracker(
            replace=False,
            daemon=daemon,
            on_track=self.on_track,
            on_recognition=self.on_recognition
        )

        self.last_recognition_id = None
        self.HDProducer = StingHumanDetectionProducer()

    def on_track(self, frame, object_center, object_offset, image_dim):
        self.robot_controller.compensate(object_center, object_offset, image_dim)

        # if frame is not None:
        #     byte_image = cv2.imencode('.jpg', frame)[1].tostring()
        #     self.HDProducer.produce(byte_image)

    def on_recognition(self, frame, label, recognition_id):
        if recognition_id != self.last_recognition_id:
            self.last_recognition_id = recognition_id

            if frame is not None:
                byte_image = cv2.imencode('.jpg', frame)[1].tostring()
                self.HDProducer.produce(byte_image)

    def process(self, frame):
        if not self.should_process():
            return None

        if self.restart:
            self.restart = False
            # self.restart = False
            # self.tracker.tracker = None

        small_frame = imutils.resize(frame, width=300)
        small_frame = cv2.rotate(small_frame, cv2.cv2.ROTATE_180)
        frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        if self.daemon:
            self.tracker.run_thread(frame)
        else:
            frame = self.tracker.track_and_detect(frame)

        if self.tracker.recognition_id != self.last_recognition_id:
            self.last_recognition_id = self.tracker.recognition_id

            if self.tracker.current_cropped_frame is not None and not self.tracker.current_cropped_frame.empty():
                byte_image = cv2.imencode('.jpg', self.tracker.current_cropped_frame)[1].tostring()
                self.HDProducer.produce(byte_image)

        self.yield_val = (
            self.tracker.object_offset,
            self.tracker.object_center,
            self.tracker.image_center,
            self.tracker.image_dim
        )

        return frame
