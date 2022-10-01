from flask import Flask, Blueprint, render_template, request, redirect, url_for
import json

from config import config
from src.delivery.context import create_context

sec = Blueprint('sec', __name__)


@sec.route('/recordings', methods=["GET"])
def recordings():
    return render_template(
        'recordings.html',
        dashboard_data=json.dumps({
            'context': create_context('sec.recordings')
        })
    )


@sec.route('/window_openers')
def window_openers():
    return render_template(
        'window_openers.html',
        dashboard_data=json.dumps({
            'context': create_context('sec.window_openers'),
            'window_openers': config['window_openers']
        })
    )


@sec.route('/single', methods=["GET"])
def single():
    camera = request.args.get('r', default="0", type=int)

    return render_template(
        'single.html',
        dashboard_data=json.dumps({
            'context': create_context('sec.single'),
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
            'context': create_context('sec.single_video'),
            'camera': camera,
            'web_path': web_path,
            'recording': recording
        })
    )


@sec.route('/cameras', methods=["GET"])
def cameras():
    return render_template('cameras.html', dashboard_data=json.dumps({
        'context': create_context('sec.cameras'),
        'cameras': config['cameras']
    }))


@sec.route('/relays', methods=["GET"])
def relays():
    return render_template('relays.html', dashboard_data=json.dumps({
        'context': create_context('sec.relays'),
        'cameras': config['cameras']
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
