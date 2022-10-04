from flask import url_for


def create_context(current_page: str, cameras: list) -> dict:
    context = {'routes': {
        'main': {
            'home': url_for('sec.index'),
            'cameras': url_for('sec.cameras'),
            'relays': url_for('sec.relays'),
            'single_cam': url_for('sec.single'),
            'window_openers': url_for('sec.window_openers')
        },
        'api': {
            'delete_rec': url_for('sec.api.delete_rec'),
            'recording_status': url_for('sec.api.recording_status'),
            'stop_record': url_for('sec.api.stop_record', camera=999),
            'start_record': url_for('sec.api.start_record', camera=999),
            'delete_record': url_for('sec.api.delete_record', camera=999, recording="###"),
            'open_window': url_for('sec.api.open_window', window_opener_name="###"),
            'close_window': url_for('sec.api.close_window', window_opener_name="###"),
            'window_step_up': url_for('sec.api.window_step_up', window_opener_name="###"),
            'window_step_down': url_for('sec.api.window_step_down', window_opener_name="###"),
            'window_open_to': url_for('sec.api.window_open_to', window_opener_name="###", open_value=999),
            'relay_status': url_for('sec.api.relay_status'),
            'relay_on': url_for('sec.api.relay_on', relay=999),
            'relay_off': url_for('sec.api.relay_off', relay=999),
        }
    }, 'menu': [
        {"route": url_for('sec.index'), "name": "Home"},
        {"route": url_for('sec.cameras'), "name": "Cameras"},
        {"route": url_for('sec.recordings'), "name": "Recordings"},
        {"route": url_for('sec.window_openers'), "name": "Window Openers"},
        {"route": url_for('sec.relays'), "name": "Relays"},
        {"route": url_for('sec.utils'), "name": "Utils"}
    ],
        'current_url': url_for(current_page),
        'cameras': cameras
    }

    return context
