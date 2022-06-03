from src.cam.CamLoader import CamLoader
from src.image.processors.TrackerProcessor import TrackerProcessor
from config import config
import math

sting_cam_url = config["cameras"][1]["source"]
safe_distance = 120


def should_handle():
    return True


def handle_tracked_object(yield_val):
    global safe_distance

    if not should_handle():
        return

    if not yield_val:
        return

    face_offset, face_center, image_center, image_dim = yield_val

    if not face_offset or not image_dim:
        return

    if not safe_distance:
        (_, h) = image_dim
        safe_distance = h/3

    x_offset, y_offset = face_offset

    distance = math.sqrt(x_offset ** 2 + y_offset ** 2)

    if distance > safe_distance:
        move_y = 0
        move_x = 0
        print(x_offset, y_offset)
        print('out')

    print('distance', distance)


if __name__ == '__main__':
    loader = CamLoader(sting_cam_url, by_url=True)
    loader.add_processor(TrackerProcessor(0, False))
    loader.add_action(TrackerProcessor.__name__, handle_tracked_object)
    loader.start()

