import time
import cv2

from src.cam.Loader import Loader


class CamLoader(Loader):
    def __init__(self, camera_id, event=None, by_url=False):
        self.event = event
        self.vs = None
        self.t = None
        self.outputFrame = None
        self.by_url = by_url
        self.frame = None

        super().__init__(refresh_rate=0.1, camera_id=camera_id)

    def get_frame(self):
        _, frame = self.vs.read()

        # self.vs.update()
        return frame

    def start_read(self):
        print("Starting thread for camera id:" + str(self.camera_id))

        try:
            if not self.by_url:
                self.vs = cv2.VideoCapture(self.camera_id)
                self.vs.set(cv2.CAP_PROP_BUFFERSIZE, 2)
                time.sleep(1)
                print("Stream for:" + str(self.camera_id) + " started, writing to buffer")
            else:
                self.vs = cv2.VideoCapture(self.camera_id)
                self.vs.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        except:
            print("Something happened ")
        
        self.read()

    def prepare_output_frame(self, frame):
        ret, buffer = cv2.imencode('.jpg', frame)
        output = buffer.tobytes()

        return output
