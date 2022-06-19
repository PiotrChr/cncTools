from src.cam.CamLoader import CamLoader
from src.cam.KafkaLoader import KafkaLoader
from src.image.processors.TrackerProcessor import TrackerProcessor
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

#
# def should_handle():
#     global current_lock
#
#     if current_lock < frame_lock:
#         current_lock = current_lock + 1
#         return False
#
#     return True
#
#
# def move_servo(motor, direction=1):
#     http.request('GET', config["cameras"][1]["move"]["motors"][motor] + '/' + str(direction))
#
#
# def handle_tracked_object(yield_val):
#     global safe_distance_w
#     global safe_distance_h
#     global current_lock
#
#     if not yield_val:
#         return
#
#     face_offset, face_center, image_center, image_dim = yield_val
#
#     if not face_offset or not image_dim:
#         return
#
#     if not safe_distance_w:
#         w, h = image_dim
#         safe_distance_h = h/5
#         safe_distance_w = w/3
#
#     x_offset, y_offset = face_offset
#
#     if should_handle():
#         if abs(x_offset) > safe_distance_w:
#             current_lock = 0
#             move_servo("h", 1 if x_offset < 0 else -1)
#
#         if abs(y_offset) > safe_distance_h:
#             current_lock = 0
#             move_servo("v", 1 if y_offset < 0 else -1)
#
#         if current_lock is 0:
#             processor.restart = True
#

# app = Flask(__name__)
#
#
# def generate_frames():
#     while True:
#         if loader.outputFrame is None:
#             time.sleep(1)
#             continue
#
#         time.sleep(0.1)
#         yiel (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + loader.outputFrame + b'\r\n')
#
#
# @app.route('/')
# def frames():
#     return Response(generate_frames(),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    kafka_loader = KafkaLoader(['StingFrames'], config["kafka"]["object_detector_conf"])
    kafka_loader.add_processor(TrackerProcessor(daemon=True))
    kafka_loader.start()

    # app.run(host="0.0.0.0", port=8888, debug=True, use_reloader=False)
