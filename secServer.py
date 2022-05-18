from flask import Flask, Blueprint, render_template, jsonify, request, url_for, redirect
from config import config
import urllib3
import json
import time
from src.cam.CamRecorder import CamRecorder
from src.delivery.http.utils import map_recorder
from os import listdir, remove
from os.path import isfile, join, exists


sec = Blueprint('sec', __name__)
main = Blueprint('main', __name__)
api = Blueprint('api', __name__)

http = urllib3.PoolManager()

recorders = []


def record(camera: int):
    for recorder in recorders:
        if recorder.camera == camera:
            print('Already recording')
            return None

    _recorder = CamRecorder(camera, config['cameras'][camera]['source'], on_stop=lambda: cleanup_recording(camera))
    _recorder.start()
    recorders.append(_recorder)


def get_rec_status_for_cam(camera: int):
    return dict(
        (_recorder.camera, map_recorder(_recorder)) for _recorder in recorders if _recorder.camera == camera
    )


def get_recordings_for_cam(camera: int):
    rec_path = config["recordings_dir"] + '/' + str(camera)
    web_path = config["recordings_dir_web"] + '/' + str(camera)

    if exists(rec_path):
        return [{"file": f, "file_path": rec_path + '/' + f, "web_path": web_path + '/' + f}
                for f in listdir(rec_path) if isfile(join(rec_path, f))]

    return None


def get_full_status_for_cam(camera: int):
    rec_status = get_rec_status_for_cam(camera)
    _recordings = get_recordings_for_cam(camera)

    if not rec_status:
        rec_status = None
    else:
        rec_status = rec_status[camera]

    return rec_status, _recordings


def cleanup_recording(camera: int):
    key, recorder = get_recorder_by_id(camera)
    recorders.pop(key)


def get_recorder_by_id(camera: int):
    for key, recorder in enumerate(recorders):
        if recorder.camera == camera:
            return key, recorder

    return None, None


def start_record(camera: int):
    _, recorder = get_recorder_by_id(camera)
    if recorder:
        return False

    record(camera)

    time.sleep(0.5)
    return True


def stop_record(camera: int):
    _, recorder = get_recorder_by_id(camera)

    if not recorder:
        return False

    recorder.halt()

    time.sleep(0.5)
    return True


def delete_record(camera: int, recording: str):
    rec_path = config["recordings_dir"] + '/' + str(camera) + '/' + recording

    if exists(rec_path) and isfile(rec_path):
        remove(rec_path)


@api.route('/', methods=["GET"])
def api_root():
    return "Api is on"


@api.route('/rec/delete/', methods=["DELETE"])
def delete_rec():
    pass


@api.route('/rec/status', methods=["GET"])
def recording_status():
    rec_status = dict((_recorder.camera, map_recorder(_recorder)) for _recorder in recorders)
    _recordings = dict((_cam, get_recordings_for_cam(_cam)) for _cam in config['cameras'])

    return {"recordings": _recordings, "status": rec_status}, 200


@api.route('/rec/stop/<int:camera>', methods=["GET"])
def api_stop_record(camera: int):
    if not stop_record(camera):
        return {"data": {"error": "Camera not recording"}}, 400

    return {"data": {"status": "Camera stopped recording"}}, 201


@api.route('/rec/start/<int:camera>', methods=["GET"])
def api_start_record(camera: int):
    if not start_record(camera):
        return {"data": {"error": "Camera" + "already recording"}}, 400

    return {"data": {"status": "Camera started recording"}}, 200


@sec.route('/rec/delete/<int:camera>/<string:recording>', methods=["GET"])
def sec_delete_record(camera: int, recording: str):
    delete_record(camera, recording)

    return redirect(url_for('sec.single', r=camera))


@sec.route('/rec/stop/<int:camera>', methods=["GET"])
def sec_stop_record(camera: int):
    if stop_record(camera):
        return redirect(url_for('sec.single', r=camera))

    return "Error"


@sec.route('/rec/start/<int:camera>', methods=["GET"])
def sec_start_record(camera: int):
    if start_record(camera):
        return redirect(url_for('sec.single', r=camera))

    return "Error"


@sec.route('/recordings/play/<string:recording>', methods=["GET"])
def play_recording(recording: str):
    pass


@sec.route('/recordings', methods=["GET"])
def recordings():
    pass


@sec.route('/relays/on/<int:relay>', methods=["GET"])
def relay_on(relay):
    on_request = http.request('GET', config['relays']['on_url'], fields={"r": relay})
    print(on_request.status)
    return redirect(url_for('sec.relays'))


@sec.route('/relays/off/<int:relay>', methods=["GET"])
def relay_off(relay):
    off_request = http.request('GET', config['relays']['off_url'], fields={"r": relay})
    print(off_request.status)

    return redirect(url_for('sec.relays'))


@sec.route('/relays', methods=["GET"])
def relays():
    # get status, decorate config and pass to template
    status_request = http.request('GET', config['relays']['status_url'])
    data = json.loads(status_request.data.decode('utf-8'))

    return render_template('relays.html', relays=config['relays']['circuits'], status=data['status'])


@sec.route('/single', methods=["GET"])
def single():
    camera = request.args.get('r', default="0", type=int)
    rec_status, _recordings = get_full_status_for_cam(camera)

    return render_template(
        'single.html',
        camera=config['cameras'][camera],
        rec_status=rec_status,
        recordings=_recordings
    )


@sec.route('/single_video', methods=["GET"])
def single_video():
    camera = request.args.get('camera', default="0", type=int)
    recording = request.args.get('recording', default="0", type=str)

    web_path = config['recordings_dir_web'] + '/' + str(camera) + '/' + recording

    return render_template(
        'single_video.html',
        camera=camera,
        web_path=web_path,
        recording=recording
    )


@sec.route('/', methods=["GET"])
def index():
    return render_template('index.html', cameras=config['cameras'])


@main.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e), url=request.url), 404


app = Flask(__name__)
sec.register_blueprint(api, url_prefix="/api")
app.register_blueprint(sec, url_prefix="/sec")
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, use_reloader=False)
