from os.path import isfile, join, exists
from os import listdir, remove
import threading
import time


from src.cam.CamRecorder import CamRecorder
from config import config, get_cam_by_id
from src.delivery.http.utils import map_recorder


class RecorderManager:
    recorders = []
    read_lock: threading.Lock
    
    def __init__(self):
        self.read_lock = threading.Lock()

    def record(self, camera: int) -> None:
        cam_config = get_cam_by_id(camera)
        
        for recorder in self.recorders:
            if recorder.camera == camera:
                print('Already recording')
                return None

        _recorder = CamRecorder(
            camera,
            cam_config['source'],
            on_stop=lambda: self.cleanup_recording(camera)
        )
        _recorder.start()
        self.recorders.append(_recorder)

    def get_rec_status_for_cam(self, camera: int) -> dict:
        return dict(
            (_recorder.camera, map_recorder(_recorder)) for _recorder in self.recorders if _recorder.camera == camera
        )

    def get_rec_status(self):
        self.read_lock.acquire()
        rec_status = (
            dict((_recorder.camera, map_recorder(_recorder)) for _recorder in self.recorders),
            list(dict({"id": _cam['id'], "recordings": self.get_recordings_for_cam(
                _cam['id'])}) for _cam in config['cameras'])
        )
        self.read_lock.release()
        
        return rec_status

    def get_recordings_for_cam(self, camera: int):
        rec_path = config["recordings_dir"] + '/' + str(camera)
        web_path = config["recordings_dir_web"] + '/' + str(camera)

        if exists(rec_path):
            return [{"file": f, "file_path": rec_path + '/' + f, "web_path": web_path + '/' + f}
                    for f in listdir(rec_path) if isfile(join(rec_path, f))]

        return None

    def get_full_status_for_cam(self, camera: int):
        self.read_lock.acquire()
        rec_status = self.get_rec_status_for_cam(camera)
        _recordings = {"id": camera, "recordings": self.get_recordings_for_cam(camera)}

        if not rec_status:
            rec_status = None
        else:
            rec_status = rec_status[camera]

        self.read_lock.release()
        
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
        self.read_lock.acquire()
        _, recorder = self.get_recorder_by_id(camera)
        if recorder:
            return False

        self.record(camera)

        time.sleep(0.5)
        self.read_lock.release()
        return True

    def stop_record(self, camera: int) -> bool:
        self.read_lock.acquire()
        key, recorder = self.get_recorder_by_id(camera)

        if not recorder:
            return False

        recorder.halt()
        time.sleep(0.5)

        del self.recorders[key]
        self.read_lock.release()
        
        return True

    def delete_record(self, camera: int, recording: str) -> None:
        self.read_lock.acquire()
        rec_path = config["recordings_dir"] + '/' + str(camera) + '/' + recording

        if exists(rec_path) and isfile(rec_path):
            remove(rec_path)
        
        self.read_lock.release()
