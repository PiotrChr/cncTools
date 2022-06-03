import threading
import time
import cv2
from imutils.video import VideoStream


class CamLoader(threading.Thread):
    def __init__(self, camera_id, event=None):
        self.camera_id = camera_id
        self.event = event
        self.vs = None
        self.t = None
        self.outputFrame = None
        self.processors = []
        self.actions = {}
        self.redetect_radius = None

        print("Created cam loader with id:" + str(camera_id))

        super().__init__()

    def add_processor(self, processor):
        self.processors.append(processor)

    def add_action(self, processor, action):
        self.actions[processor] = action

    def start(self):
        self.t = threading.Thread(
            target=self.start_read,
            daemon=True,
        )
        self.t.start()

    def start_read(self):
        print("Starting thread for camera id:" + str(self.camera_id))
        self.vs = VideoStream(src=self.camera_id).start()
        time.sleep(2)
        print("Stream for:" + str(self.camera_id) + " started, writing to buffer")

        self.read()

    def read(self):
        frame = self.vs.read()

        if frame is None:
            return
        else:
            for processor in self.processors:
                process = processor.process(frame)
                if process is None:
                    continue

                frame = process
                processor_name = processor.__class__.__name__
                if self.actions[processor_name]:
                    self.actions[processor_name](processor.yield_val)

            ret, buffer = cv2.imencode('.jpg', frame)
            self.outputFrame = buffer.tobytes()

        t = threading.Timer(0.05, self.read)
        t.daemon = True
        t.start()