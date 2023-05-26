import time

from flask import Flask, Blueprint, Response, jsonify, request, make_response, abort
import threading
import argparse
from src.cam.Loader import Loader
from src.cam.CamLoader import CamLoader
from src.cam.KafkaLoader import KafkaLoader
from config import config

lock = threading.Lock()

loaders = []

cam = Blueprint('cam', __name__)
main = Blueprint('main', __name__)


def get_loader(camera_id):
    for _loader in loaders:
        if _loader.camera_id == camera_id:
            return _loader

    return None


def generate_frames(camera_id):
    _loader: Loader = get_loader(camera_id)
    if _loader is None:
        raise Exception("No loader with id: " + str(camera_id) + " found")
    
    static = False

    # if isinstance(_loader, CamLoader):
    #     static = True

    outputFrame = _loader.get_output_frame(False)

    # print(outputFrame)
    if outputFrame is None:
        print("No output for camera: " + str(camera_id))
        abort(404)

    return outputFrame


@cam.route('/video_feed/<string:camera_id>/', methods=["GET"])
def video_feed(camera_id):
    """Video streaming route. Put this in the src attribute of an img tag."""

    print('Trying to get frame for camera: ' + str(camera_id))

    # Try converting to int if it's a number, otherwise carry on with str index
    try:
        camera_id = int(camera_id)
    except:
        pass

    response = make_response(generate_frames(camera_id))
    response.headers['Content-Type'] = 'image/png'

    return response


@main.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e), url=request.url, details="Cam resource was not found"), 404


app = Flask(__name__)
app.register_blueprint(cam, url_prefix="/cam")
app.register_blueprint(main)

if __name__ in ['__main__', 'uwsgi_file_camLoader']:
    ap = argparse.ArgumentParser()
    ap.add_argument('-c', '--cameras', nargs='+', type=str, required=True)
    for _, value in ap.parse_args()._get_kwargs():
        if _ == "cameras":
            for cam in value:
                try:
                    cam = int(cam)
                    loader = CamLoader(cam)
                    loader.start()
                except ValueError:
                    loader = KafkaLoader([cam], config["kafka"]["frame_consumer_conf"])
                    loader.start()
                
                loaders.append(loader)

    if __name__ == "__main__":
        app.run(host="0.0.0.0", debug=True, use_reloader=False)


