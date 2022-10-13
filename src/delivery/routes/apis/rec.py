from flask import Flask, Blueprint
import urllib3
import json

from config import config
from src.services.RecorderManager import RecorderManager

http = urllib3.PoolManager()
rec = Blueprint('rec', __name__)


recorder_manager = RecorderManager()


@rec.route('/delete/<int:camera>/<string:recording>/', methods=["DELETE"])
def delete_rec(camera: str, recording: int):
    recorder_manager.delete_record(camera, recording)
    
    return {"data": {"status": "Recording was removed"}}, 200


@rec.route('/status/', methods=["GET"])
def recording_status():
    rec_status, recordings = recorder_manager.get_rec_status()

    return {"data": {"recordings": recordings, "status": rec_status}}, 200


@rec.route('/status/<int:camera>/', methods=["GET"])
def recording_status_for_cam(camera: int):
    rec_status, recordings = recorder_manager.get_full_status_for_cam(camera)

    return {"data": {"recordings": recordings, "status": rec_status, "camera": camera}}, 200


@rec.route('/stop/<int:camera>/', methods=["GET"])
def stop_record(camera: int):
    if not recorder_manager.stop_record(camera):
        return {"data": {"error": "Camera not recording"}}, 400

    return {"data": {"status": "Camera stopped recording"}}, 201


@rec.route('/start/<int:camera>/', methods=["GET"])
def start_record(camera: int):
    if not recorder_manager.start_record(camera):
        return {"data": {"error": "Camera" + "already recording"}}, 400

    return {"data": {"status": "Camera started recording"}}, 200


@rec.route('/delete/<int:camera>/<string:recording>/', methods=["GET"])
def delete_record(camera: int, recording: str):
    recorder_manager.delete_record(camera, recording)

    return {"data": {"status": "Camera recording removed"}}, 200
