from imutils.video import VideoStream
from src.cam.Loader import Loader


class StaticCamLoader(Loader):
    def __init__(self, camera_id) -> None:
        self.vs = VideoStream(src=self.camera_id, framerate=10).start()

    def get_frame(self):
        pass

    def start_read():
        pass



