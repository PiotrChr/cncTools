import os

base_dirs = {
    "web_root": "/sec",
    "root_dir": os.path.abspath(os.curdir),
    "recordings_dir_rel": "/static/recordings",
    "recordings_dir_web": "/recordings"
    }

base_dirs["recordings_dir"] = base_dirs["root_dir"] + base_dirs["recordings_dir_rel"]

config = {
    **base_dirs,
    "cameras": {
        0: {
            "id": 0,
            "name": "6040 CNC",
            "source": "http://192.168.2.53:8081/cam/video_feed/4",
        },
        1: {
            "id": 1,
            "name": "Sting",
            "source": "http://192.168.2.55:8081/cam/video_feed/0",
            "move": {
                "motors": {
                    "v": "http://192.168.2.55:8082/api/move/0",
                    "h": "http://192.168.2.55:8082/api/move/1"
                }
            }
        },
        2: {
            "id": 2,
            "name": "PiHouse",
            "source": "http://192.168.2.47:8081/cam/video_feed/0",
        },
        3: {
            "id": 3,
            "name": "Workshop 1",
            "source": "http://192.168.2.53:8081/cam/video_feed/0",
        },
        4: {
            "id": 4,
            "name": "Workshop 2",
            "source": "http://192.168.2.53:8081/cam/video_feed/2",
        },
        5: {
            "id": 5,
            "name": "3D printer 1",
            "source": "http://192.168.2.43/webcam/?action=stream",
            "rotate": 180
        },
        6: {
            "id": 6,
            "name": "3D printer 2",
            "source": "http://192.168.2.43:8081/1action=stream",
        },
        7: {
            "id": 7,
            "name": "Pigeon Cam",
            "source": "http://192.168.2.60:8081/cam/video_feed/0",
            "rotate": 180
        }
    },
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
    "window_openers": {
        "living_room_1": {
            "id": 1,
            "source": "192.168.2.61",
            "name": "Living room 1"
        }
    }
}
