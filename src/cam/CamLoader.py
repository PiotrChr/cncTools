import threading
import time
import cv2
from imutils.video import VideoStream
import urllib3
import numpy as np

http = urllib3.PoolManager()


class CamLoader(threading.Thread):
    def __init__(self, camera_id, event=None, by_url=False):
        self.camera_id = camera_id
        self.event = event
        self.vs = None
        self.t = None
        self.outputFrame = None
        self.processors = []
        self.actions = {}
        self.redetect_radius = None
        self.by_url = by_url

        print("Created cam loader with id:" + str(camera_id))

        super().__init__()

    def add_processor(self, processor):
        self.processors.append(processor)

    def add_action(self, processor, action):
        self.actions[processor] = action

    def start(self):
        self.t = threading.Thread(
            target=self.start_read,
            daemon=False,
        )
        self.t.start()

    def get_frame(self):
        if self.by_url:
            # url_response = http.request('GET', self.camera_id)
            # print(url_response.read())
            # arr = np.asarray(bytearray(url_response.read()), dtype=np.uint8)
            #
            # return cv2.imdecode(arr, -1)
            _, frame = self.vs.read()

            return frame
        else:
            return self.vs.read()

    def start_read(self):
        print("Starting thread for camera id:" + str(self.camera_id))

        if not self.by_url:
            self.vs = VideoStream(src=self.camera_id).start()
            time.sleep(2)
            print("Stream for:" + str(self.camera_id) + " started, writing to buffer")
        else:
            self.vs = cv2.VideoCapture(self.camera_id)

        self.read()

    def read(self):
        frame = self.get_frame()

        if frame is None:
            print('No frame')
        else:
            print('checking processors')
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
        t.daemon = False
        t.start()
