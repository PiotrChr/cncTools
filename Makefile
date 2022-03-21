CNCIP := 192.168.2.53
CNCUSER := pchrusciel
CNCFOLDER := /home/pchrusciel/cncTools

start_vnc:
	x11vnc -display :0

install_cam:
	pip3 install -r requirements.txt

test_cam:
	python3 scripts/testcam.py

start_stream:
	python3 app.py

sync_cnc:
	rsync -av --exclude={'.git/*','venv/'} ./ ${CNCUSER}@${CNCIP}:${CNCFOLDER}
