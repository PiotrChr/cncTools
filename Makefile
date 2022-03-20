start_vnc:
	x11vnc -display :0

install_cam:
    pip3 install -r requirements.txt

start_stream:
    python3 app.py
