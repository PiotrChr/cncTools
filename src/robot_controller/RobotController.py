import urllib3
import json
from config import config

http = urllib3.PoolManager()


class RobotController:
    FRAME_LOCK = 10
    H_RANGE = range(0, 1)
    W_RANGE = range(0, 1)
    H_ANGLE = 50
    V_ANGLE = 20
    MOTOR_V = 0
    MOTOR_H = 1

    def __init__(self):
        self.current_lock = 0
        self.safe_h = None
        self.safe_w = None
        self.h_step = None
        self.v_step = None

    def compensate(self, object_center, object_offset, image_dim):
        print("running compensate on track")
        # if not self.should_handle():
        #     return

        if not self.safe_w:
            w, h = image_dim
            self.safe_h = h/5
            self.safe_w = w/3
            self.h_step = self.H_ANGLE/w
            self.v_step = self.V_ANGLE/h

        x_offset, y_offset = object_offset

        if abs(x_offset) <= self.safe_w and abs(y_offset) <= self.safe_h:
            return

        pos_v, pos_h = self.readpos()

        # TODO: Finish this
        # motor = 0
        # angle = 0
        # if abs(x_offset) > self.safe_w:
        #     self.current_lock = 0
        #     motor = self.MOTOR_H
        #     # self.move_camera("h", 1 if x_offset < 0 else -1)
        #     print('w out')
        #
        # if abs(y_offset) > self.safe_h:
        #     self.current_lock = 0
        #     motor = self.MOTOR_H
        #     # self.move_camera("v", 1 if y_offset < 0 else -1)
        #     print('h out')
        #
        # self.move_camera(motor, angle)

    def should_handle(self):
        if self.current_lock < self.FRAME_LOCK:
            self.current_lock = self.current_lock + 1
            return False

        return True

    def move_camera(self, motor, angle):
        url = "%s%s/%s/%s/" % (config["cameras"][1]["api"], 'move', motor, angle)
        res = http.request('GET',  url)

    def step(self, motor, direction=0):
        url = "%s%s/%s/%s/" % (config["cameras"][1]["api"], 'step', motor, direction)
        res = http.request('GET',  url)

    def idle_move(self):
        res = http.request('GET', config["cameras"][1]["api"] + 'idle/')

    def auto_idle_on(self):
        res = http.request('GET', config["cameras"][1]["api"] + 'auto_idle_on/')

    def auto_idle_off(self):
        res = http.request('GET', config["cameras"][1]["api"] + 'auto_idle_off/')

    def reset(self):
        http.request('GET', config["cameras"][1]["api"] + 'reset/')

    def readpos(self):
        res = http.request('GET', config["cameras"][1]["api"] + 'readpos/')
        position = (json.loads(res.data))['position']

        return position['v'], position['h']
