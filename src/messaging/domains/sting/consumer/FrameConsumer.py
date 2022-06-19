from src.messaging.Consumer import Consumer
from config import config
import cv2
import numpy as np


class FrameConsumer(Consumer):
    def __init__(self, topics, conf=config["kafka"]["frame_consumer_conf"]):
        super().__init__(topics, conf)

    def process(self, msg):
        frame = cv2.imdecode(np.fromstring(msg.value(), dtype=np.uint8), cv2.IMREAD_UNCHANGED)

        return frame
