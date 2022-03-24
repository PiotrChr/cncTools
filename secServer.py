from flask import Flask, Blueprint, render_template, jsonify, request

sec = Blueprint('sec', __name__)
main = Blueprint('main', __name__)


@sec.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@main.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e), url=request.url), 404


app = Flask(__name__)
app.register_blueprint(sec, url_prefix="/sec")
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, use_reloader=False)


