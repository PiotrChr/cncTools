from src.cam.KafkaLoader import KafkaLoader
from src.image.processors.TrackerProcessor import TrackerProcessor
from config import config, get_cam_by_id
import time
import urllib3

http = urllib3.PoolManager()

sting_cam_url = get_cam_by_id(1)["source"]
safe_distance_w = None
safe_distance_h = None
frame_lock = 10
current_lock = 0


if __name__ == '__main__':
    kafka_loader = KafkaLoader(['StingFrames'], config["kafka"]["object_detector_conf"])
    kafka_loader.add_processor(TrackerProcessor(daemon=True))
    kafka_loader.start()

