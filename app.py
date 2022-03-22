from flask import Flask, Blueprint, render_template, Response, jsonify, request
import cv2

sec = Blueprint('sec', __name__)
main = Blueprint('main', __name__)


def gen_frames(camera_id):
    cap = cv2.VideoCapture(camera_id)
    
    while True:
        # for cap in caps:
        # # Capture frame-by-frame
        success, frame = cap.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@sec.route('/video_feed/<int:camera_id>/', methods=["GET"])
def video_feed(camera_id):
   
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(camera_id),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


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
    app.run(host="0.0.0.0", debug=True)


