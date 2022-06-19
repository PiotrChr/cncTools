import dlib
from src.image.utils import convert_and_trim_bb
import cv2
import imutils


class FaceDetector:
    def __init__(self, upsample=0):
        self.detector = dlib.get_frontal_face_detector()
        self.upsample = upsample
        self.detection =

    def detect(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.detection = self.detector(rgb, self.upsample)

        return frame

