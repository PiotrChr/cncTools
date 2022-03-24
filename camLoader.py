import time

from flask import Flask, Blueprint, Response, jsonify, request
import threading
import argparse
from src.cam.CamLoader import CamLoader

outputFrame = None
lock = threading.Lock()

frameRate = 30

loaders = []

cam = Blueprint('cam', __name__)
main = Blueprint('main', __name__)


def get_loader(camera_id):
    for _loader in loaders:
        if _loader.camera_id == camera_id:
            return _loader

    return None


def generate_frames(camera_id):
    _loader = get_loader(camera_id)
    if _loader is None:
        raise Exception("No loader with id: " + camera_id + " found")

    while True:
        if _loader.outputFrame is None:
            time.sleep(1)
            continue

        time.sleep(0.1)
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + _loader.outputFrame + b'\r\n')


@cam.route('/video_feed/<int:camera_id>/', methods=["GET"])
def video_feed(camera_id):
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(generate_frames(camera_id),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@main.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e), url=request.url, details="Cam resource was not found"), 404


app = Flask(__name__)
app.register_blueprint(cam, url_prefix="/cam")
app.register_blueprint(main)

if __name__ in ['__main__', 'uwsgi_file_camLoader']:
    ap = argparse.ArgumentParser()
    ap.add_argument('-c', '--cameras', nargs='+', type=int, required=True)
    print("args")
    print(ap.parse_args()._get_kwargs())
    for _, value in ap.parse_args()._get_kwargs():
        print(value)
        if _ == "cameras":
            for cam in value:
                loader = CamLoader(cam)
                loader.start()
                loaders.append(loader)

    if __name__ == "__main__":
        app.run(host="0.0.0.0", debug=True, use_reloader=False)


