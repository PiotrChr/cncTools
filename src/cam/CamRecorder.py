import threading
import cv2
import numpy as np
from datetime import datetime
from config import config
import os


class CamRecorder(threading.Thread):
    def __init__(self, camera, source, timer=None, on_stop=None):
        self.camera = camera
        self.source = source
        self.timer = timer
        self.t = None
        self._camera = config["cameras"][camera]
        self.vcap = None
        self.stop = None
        self._out = None
        self.height = None
        self.width = None
        self.recording_name = None
        self.file_name = None
        self.temp_prefix = "temp_"
        self.temp_file_name = None
        self.web_path = None
        self.started_at = None
        self.on_stop = on_stop
        self.fps = 20

        super().__init__(name="camera_recording_" + str(camera))

    def halt(self):
        self.stop = True

    def start(self):
        self.t = threading.Thread(
            target=self.start_record,
            daemon=True,
        )
        self.t.start()

    def generate_temp_filename(self, started_at):
        return self.temp_prefix + self.generate_file_name(started_at)

    def generate_file_name(self, started_at):
        return "Camera_" + str(self.camera) + "_recording_" + started_at.strftime("%d-%m-%Y_%H-%M-%S") + '.mp4'

    def prepare(self):
        camera_path = config['recordings_dir'] + "/" + str(self.camera)
        self.started_at = datetime.now()
        if not os.path.exists(camera_path):
            os.makedirs(camera_path)

        self.recording_name = self.generate_file_name(self.started_at)
        self.web_path = config['recordings_dir_web'] + self.recording_name
        self.temp_file_name = camera_path + '/' + self.generate_temp_filename(self.started_at)
        self.file_name = camera_path + '/' + self.recording_name

    def start_record(self):
        self.vcap = cv2.VideoCapture(self.source)
        self.prepare()

        print("Started recording to: " + self.temp_file_name)

        if not self.vcap.isOpened():
            print("File Cannot be Opened")
            return self.end()

        while True and not self.stop:
            ret, frame = self.vcap.read()

            if frame is not None:
                self.write(frame)
            else:
                print("Frame is None")
                return self.end()

        self.end()

    def end(self):
        print("Finishing recording")

        self.vcap.release()
        self._out.release()
        cv2.destroyAllWindows()

        os.system("ffmpeg -i " + self.temp_file_name + " -vcodec libx264 " + self.file_name)
        os.remove(self.temp_file_name)

        if callable(self.on_stop):
            self.on_stop()

    def write(self, item: np.array):
        if self._out is None:
            self.height = item.shape[0]
            self.width = item.shape[1]
            self._out = cv2.VideoWriter(
                self.temp_file_name,
                cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),
                self.fps,
                (self.width, self.height)
            )

        resized = cv2.resize(item, (self.width, self.height), interpolation=cv2.INTER_AREA)

        rot_val = self._camera["rotate"]
        if rot_val == 90:
            resized = cv2.rotate(resized, cv2.cv2.ROTATE_90_CLOCKWISE)
        if rot_val == -90:
            resized = cv2.rotate(resized, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
        if rot_val == 180:
            resized = cv2.rotate(resized, cv2.cv2.ROTATE_180)

        # if self._swap_channels:
        #     resized = resized[...,::-1]
        self._out.write(resized)
