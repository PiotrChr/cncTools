from os.path import isfile, join, exists
from os import listdir, remove
import time


from src.cam.CamRecorder import CamRecorder
from config import config
from src.delivery.http.utils import map_recorder


class RecorderManager:
    recorders = []

    def __init__(self):
        pass

    def record(self, camera: int) -> None:
        for recorder in self.recorders:
            if recorder.camera == camera:
                print('Already recording')
                return None

        _recorder = CamRecorder(
            camera,
            config['cameras'][camera]['source'],
            on_stop=lambda: self.cleanup_recording(camera)
        )
        _recorder.start()
        self.recorders.append(_recorder)

    def get_rec_status_for_cam(self, camera: int) -> dict:
        return dict(
            (_recorder.camera, map_recorder(_recorder)) for _recorder in self.recorders if _recorder.camera == camera
        )

    def get_rec_status(self) -> (dict, dict):
        return (
            dict((_recorder.camera, map_recorder(_recorder)) for _recorder in self.recorders),
            dict((_cam, self.get_recordings_for_cam(_cam)) for _cam in config['cameras'])
        )

    def get_recordings_for_cam(self, camera: int):
        rec_path = config["recordings_dir"] + '/' + str(camera)
        web_path = config["recordings_dir_web"] + '/' + str(camera)

        if exists(rec_path):
            return [{"file": f, "file_path": rec_path + '/' + f, "web_path": web_path + '/' + f}
                    for f in listdir(rec_path) if isfile(join(rec_path, f))]

        return None

    def get_full_status_for_cam(self, camera: int):
        rec_status = self.get_rec_status_for_cam(camera)
        _recordings = self.get_recordings_for_cam(camera)

        if not rec_status:
            rec_status = None
        else:
            rec_status = rec_status[camera]

        return rec_status, _recordings

    def cleanup_recording(self, camera: int):
        key, recorder = self.get_recorder_by_id(camera)
        self.recorders.pop(key)

    def get_recorder_by_id(self, camera: int):
        for key, recorder in enumerate(self.recorders):
            if recorder.camera == camera:
                return key, recorder

        return None, None

    def start_record(self, camera: int):
        _, recorder = self.get_recorder_by_id(camera)
        if recorder:
            return False

        self.record(camera)

        time.sleep(0.5)
        return True

    def stop_record(self, camera: int) -> bool:
        _, recorder = self.get_recorder_by_id(camera)

        if not recorder:
            return False

        recorder.halt()
        time.sleep(0.5)

        return True

    def delete_record(self, camera: int, recording: str) -> None:
        rec_path = config["recordings_dir"] + '/' + str(camera) + '/' + recording

        if exists(rec_path) and isfile(rec_path):
            remove(rec_path)
