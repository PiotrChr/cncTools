from flask import url_for


def create_context(current_page: str, cameras: list) -> dict:
    context = {'routes': {
        'main': {
            'home': url_for('sec.index'),
            'cameras': url_for('sec.cameras'),
            'relays': url_for('sec.relays'),
            'single_cam': url_for('sec.single'),
            'window_openers': url_for('sec.window_openers')
        }
    }, 'menu': [
        {"route": url_for('sec.index'), "name": "Home"},
        {"route": url_for('sec.cameras'), "name": "Cameras"},
        {"route": url_for('sec.recordings'), "name": "Recordings"},
        {"route": url_for('sec.window_openers'), "name": "Window Openers"},
        {"route": url_for('sec.relays'), "name": "Relays"},
        {"route": url_for('sec.utils'), "name": "Utils"},
        {"route": url_for('sec.notifications'), "name": "Notifications"}
    ],
        'current_url': url_for(current_page),
        'cameras': cameras
    }

    return context
