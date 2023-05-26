from src.cam.CamLoader import CamLoader
from src.cam.KafkaLoader import KafkaLoader
from src.image.processors.FaceDetectionProcessor import FaceDetectionProcessor
from config import config
import time
from flask import Flask, Response
import urllib3
from src.messaging.domains.sting.consumer.FrameConsumer import FrameConsumer


sting_cam_url = config["cameras"][1]["source"]
safe_distance_w = None
safe_distance_h = None
frame_lock = 10
current_lock = 0
http = urllib3.PoolManager()


if __name__ == '__main__':
    kafka_loader = KafkaLoader(['StingObjectDetections'], config["kafka"]["face_detector_conf"])
    kafka_loader.add_processor(FaceDetectionProcessor())
    kafka_loader.start()

    # app.run(host="0.0.0.0", port=8888, debug=True, use_reloader=False)
