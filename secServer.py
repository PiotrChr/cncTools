from flask import Flask, Blueprint
from src.delivery.routes.api import api
from src.delivery.routes.sec import sec


def create_server():
    main = Blueprint('main', __name__)

    app = Flask(__name__)
    sec.register_blueprint(api, url_prefix="/api")
    app.register_blueprint(sec, url_prefix="/sec")
    app.register_blueprint(main)

    return app


if __name__ in ['__main__', 'uwsgi_file_secServer']:
    server = create_server()

if __name__ == '__main__':
    server.run(host="0.0.0.0", debug=True, use_reloader=False)
