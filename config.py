import os
import uuid

base_dirs = {
    "web_root": "/sec",
    "root_dir": os.path.abspath(os.curdir),
    "recordings_dir_rel": "/static/recordings",
    "recordings_dir_web": "/recordings"
    }

base_dirs["recordings_dir"] = base_dirs["root_dir"] + base_dirs["recordings_dir_rel"]

config = {
    **base_dirs,
    "cameras": [
        {
            "id": 0,
            "name": "6040 CNC",
            "type": "static",
            "source": "http://192.168.2.53:8081/cam/video_feed/4",
        },
        {
            "id": 1,
            "name": "Sting",
            "kafka": True,
            "source": "http://192.168.2.53:8081/cam/video_feed/StingFrames/",
            "api": "http://192.168.2.83:8082/api/",
            "rotate": 180,
            "type": "static",
            "detector": {
                "cam": {
                    "source": "http://192.168.2.53:8081/cam/video_feed/StingObjectDetections",
                    "id": 6
                },
                "rov": 60,
                "range": {
                    "v": 40,
                    "h": 180
                },
                "cam_position": {
                    "loc": (455, 35),
                    "def_pos_angle": 42
                },
                "room": {
                    "area": (805, 440),
                    "shape": [
                        (0, 0),
                        (0, 315),
                        (125, 315),
                        (125, 440),
                        (805, 440),
                        (805, 0)
                    ]
                },
            },
            "move": {
                "full": {
                    "h": "move/0/",
                    "v": "move/1/"
                },
                "step": {
                    "h": "step/0/",
                    "v": "step/1/"
                },
                "toggle_idle_axis": {
                    "h": "toggle_idle/0/",
                    "v": "toggle_idle/1/"
                },
                "reset": "reset/",
                "idle": "idle/",
                "stop": "stop/",
                "auto_idle_on": "auto_idle_on/",
                "auto_idle_off": "auto_idle_off/",
                "pos": "readpos/"
            }
        },
        {
            "id": 2,
            "name": "Workshop 1",
            "type": "static",
            "source": "http://192.168.2.53:8081/cam/video_feed/0",
        },
        {
            "id": 3,
            "name": "Workshop 2",
            "type": "static",
            "source": "http://192.168.2.53:8081/cam/video_feed/2",
        },
        {
            "id": 4,
            "name": "3D printer 1",
            "type": "dynamic",
            "source": "http://192.168.2.43/webcam/?action=stream",
            "rotate": 180
        },
        {
            "id": 5,
            "name": "3D printer 2",
            "type": "dynamic",
            "source": "http://192.168.2.43:8081/?action=stream",
        },
        # 6: {
        #     "id": 6,
        #     "name": "Pigeon Cam",
        #     "source": "http://192.168.2.60:8081/cam/video_feed/0",
        #     "rotate": 180
        # },
        {
            "id": 6,
            "name": "Sting Object Detections",
            "type": "static",
            "kafka": True,
            "source": "http://192.168.2.53:8081/cam/video_feed/StingObjectDetections"

        },
    ],
    "relays": {
        "status_url": "192.168.2.56/status",
        "on_url": "192.168.2.56/on",
        "off_url": "192.168.2.56/off",
        "circuits": {
            "1": {
                "alias": "Circuit 1 (CNC)",
                "id": 0,
                "status": 0
            },
            "2": {
                "alias": "Circuit 2",
                "id": 1,
                "status": 0
            },
            "3": {
                "alias": "Circuit 3",
                "id": 2,
                "status": 0
            },
            "4": {
                "alias": "Circuit 4",
                "id": 3,
                "status": 0
            }
        }
    },
    "window_openers": [
        {
            "id": 1,
            "source": "192.168.2.61",
            "name": "Living room 1"
        }
    ],
    "kafka": {
        "servers": "192.168.2.53:29092",
        "face_detector_conf": {
            "bootstrap.servers": "192.168.2.53:29092",
            "group.id": uuid.uuid4(),
            "enable.auto.commit": "False",
            "auto.offset.reset": "largest"
        },
        "object_detector_conf": {
            "bootstrap.servers": "192.168.2.53:29092",
            "group.id": uuid.uuid4(),
            "enable.auto.commit": "False",
            "auto.offset.reset": "largest"
        },
        "frame_consumer_conf": {
            "bootstrap.servers": "192.168.2.53:29092",
            "group.id": uuid.uuid4(),
            "enable.auto.commit": "False",
            "auto.offset.reset": "largest"
        },
        "notifications_consumer_conf": {
            "bootstrap.servers": "192.168.2.53:29092",
            "group.id": uuid.uuid4(),
            "enable.auto.commit": "False",
            "auto.offset.reset": "largest"
        },
        "conf": {
            "bootstrap.servers": "192.168.2.53:29092",
            "group.id": uuid.uuid4()
        },
        "topics": {
            "Notifications"
            "StingFrames",
            "StingObjectDetections",
            "StingFaceDetections",
            "StingHumanRecognitions"
        }
        
    },
    "apis": {
        "sting": "http://192.168.2.83:8082/api/"
    }
}


def get_cam_by_id(_id: int):
    for camera in config['cameras']:
        if camera['id'] == _id:
            return camera
        
    return None
