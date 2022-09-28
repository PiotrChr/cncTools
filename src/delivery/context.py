from flask import url_for

context = {
    'routes': {
        'main': {
            'home': url_for('sec.index'),
            'cameras': url_for('sec.cameras'),
            'relays': url_for('sec.relays'),
            'single_cam': url_for('sec.single'),
            'window_openers': url_for('sec.window_openers')
        },
        'api': {
            'delete_rec': url_for('sec.api.delete_rec'),
            'recording_status': url_for('sec.recording_status'),
            'stop_record': url_for('sec.stop_record'),
            'start_record': url_for('sec.start_record'),
            'delete_record': url_for('sec.delete_record'),
            'open_window': url_for('sec.open_window'),
            'close_window': url_for('sec.close_window'),
            'window_step_up': url_for('sec.window_step_up'),
            'window_open_to': url_for('sec.window_open_to'),
            'relay_status': url_for('sec.relay_status'),
            'relay_on': url_for('sec.relay_on'),
            'relay_off': url_for('sec.relay_off'),
        }
    },
    'menu': {
        "/home": "Home",
        "/cameras": "Cameras",
        "/window_openers": "Window Openers",
        "/relays": "Relays"
    },
}


def create_context(current_page: str) -> dict:
    context['current_url'] = url_for(current_page)

    return context
