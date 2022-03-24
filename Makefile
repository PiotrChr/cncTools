CNCIP := 192.168.2.53
CNCUSER := pchrusciel
CNCFOLDER := /home/pchrusciel/cncTools

start_vnc:
	x11vnc -display :0

prepare:
	sudo apt install -y python3.7-dev python3-distutils uwsgi uwsgi-src uuid-dev libcap-dev libpcre3-dev libpython3.7-dev libpython3-all-dev uwsgi-plugin-python3 \
	& pip3 install uwsgi

install_cam:
	pip3 install -r requirements.txt

test_cam:
	python3 scripts/testcam.py

start_stream:
	python3 app.py

sync_cnc:
	rsync -av --exclude={'venv','.idea','__pycache__'} ./ ${CNCUSER}@${CNCIP}:${CNCFOLDER}

start_uwsgi_cam:
	uwsgi resources/uwsgi/uwsgi_cam.ini --enable-threads

start_uwsgi_sec:
	uwsgi resources/uwsgi/uwsgi_sec.ini
