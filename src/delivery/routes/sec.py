from flask import Flask, Blueprint, render_template, request, redirect, url_for
import json

from config import config
from src.delivery.context import create_context

sec = Blueprint('sec', __name__)


@sec.route('/recordings', methods=["GET"])
def recordings():
    return render_template(
        'default.html',
        pageTitle='Recordings',
        jsFile=url_for('static', filename='js/dist/recordings.js'),
        dashboard_data=json.dumps({
            'context': create_context('sec.recordings', config['cameras'])
        })
    )


@sec.route('/utils')
def utils():
    return render_template(
        'default.html',
        pageTitle='Utils',
        jsFile=url_for('static', filename='js/dist/utils.js'),
        dashboard_data=json.dumps({
            'context': create_context('sec.utils', config['cameras'])
        })
    )


@sec.route('/window_openers')
def window_openers():
    return render_template(
        'default.html',
        pageTitle='Window Openers',
        jsFile=url_for('static', filename='js/dist/window_openers.js'),
        dashboard_data=json.dumps({
            'context': create_context('sec.window_openers', config['cameras']),
            'window_openers': config['window_openers']
        })
    )


@sec.route('/single', methods=["GET"])
def single():
    camera = request.args.get('r', default="0", type=int)

    return render_template(
        'default.html',
        pageTitle='Single Camera',
        jsFile=url_for('static', filename='js/dist/single.js'),
        dashboard_data=json.dumps({
            'context': create_context('sec.single', config['cameras']),
            'camera': config['cameras'][camera],
        })
    )


@sec.route('/single_video', methods=["GET"])
def single_video():
    camera = request.args.get('camera', default="0", type=int)
    recording = request.args.get('recording', default="0", type=str)

    web_path = config['recordings_dir_web'] + '/' + str(camera) + '/' + recording

    return render_template(
        'single_video.html',
        dashboard_data=json.dumps({
            'context': create_context('sec.single_video', config['cameras']),
            'camera': camera,
            'web_path': web_path,
            'recording': recording
        })
    )


@sec.route('/cameras', methods=["GET"])
def cameras():
    return render_template(
        'default.html', 
        pageTitle='Overseer eye',
        jsFile=url_for('static', filename='js/dist/cameras.js'),
        dashboard_data=json.dumps({
            'context': create_context('sec.cameras', config['cameras'])
    }))


@sec.route('/relays', methods=["GET"])
def relays():
    return render_template(
        'default.html',
        pageTitle='Relays',
        jsFile=url_for('static', filename='js/dist/relays.js'),
        dashboard_data=json.dumps({
            'context': create_context('sec.relays', config['cameras'])
    }))


@sec.route('/notifications', methods=["GET"])
def notifications():
    return render_template(
        'default.html',
        pageTitle='Notifications',
        jsFile=url_for('static', filename='js/dist/notifications.js'),
        dashboard_data=json.dumps({
            'context': create_context('sec.main', config['cameras'])
        }))


@sec.route('/', methods=["GET"])
def index():
    return redirect(url_for('sec.cameras'))
    # return render_template(
    #     'index.html',
    #     dashboard_data={
    #         create_context('sec.index')
    #     }
    # )
