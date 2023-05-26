from flask import Flask, Blueprint
import urllib3
from config import config
from src.robot_controller.RobotController import RobotController

http = urllib3.PoolManager()
sting = Blueprint('sting', __name__)

robot_controller = RobotController()

DEFAULT_STING_STATUS_MSG = "Command sent"


@sting.route('/status/', methods=["GET"])
def sting_status():
    try:
        status = robot_controller.status()
    except:    
        return {"data": {"error": "Error reading robot position"}}
    
    return {"data": status}, 200


@sting.route('/idle_move/', methods=["GET"])
def idle_move():
    robot_controller.idle_move()
    
    return {"data": {"status": "Idle is on"}}


@sting.route('/toggle_idle/<int:motor>/<int:value>/', methods=["GET"])
def toggle_idle(motor: int, value: int):
    robot_controller.toggle_idle(motor, value)
    
    return {"data": {"status": DEFAULT_STING_STATUS_MSG}}


@sting.route('/reset_c/', methods=["GET"])
def reset_sting_controller():
    url = config['apis']['sting'] + 'reset_dev/'
    http.request('GET', url)

    return {"data": {"status": "Sting - Ardunio was rebooted"}}, 200


@sting.route('/idle_idle_on/', methods=["GET"])
def auto_idle_on():
    robot_controller.auto_idle_on()

    return {"data": {"status": "Auto idle is on"}}


@sting.route('/auto_idle_off/', methods=["GET"])
def auto_idle_off():
    robot_controller.auto_idle_off()
    
    return {"data": {"status": "Auto idle is off"}}


@sting.route('/reset', methods=["GET"])
def reset():
    robot_controller.reset()

    return {"data": {"status": DEFAULT_STING_STATUS_MSG}}


@sting.route('/step/<int:motor>/<string:direction>', methods=["GET"])
def step(motor: int, direction: int):
    robot_controller.step(motor, int(direction))
    
    return {"data": {"status": DEFAULT_STING_STATUS_MSG}}

    
@sting.route('/move/<int:motor>/<int:angle>/', methods=["GET"])    
def move(motor: int, angle: int):
    robot_controller.move_camera(motor, angle)
    
    return {"data": {"status": DEFAULT_STING_STATUS_MSG}}


@sting.route('/idle_speed/<int:speed>/', methods=["GET"])    
def idle_speed(motor: int, angle: int):
    robot_controller.move_camera(motor, angle)
    
    return {"data": {"status": DEFAULT_STING_STATUS_MSG}}


@sting.route('/stop/', methods=["GET"])    
def stop():
    robot_controller.stop()
    
    return {"data": {"status": DEFAULT_STING_STATUS_MSG}}
