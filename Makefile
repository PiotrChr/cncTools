CNCIP := 192.168.2.53
CNCUSER := pchrusciel
CNCFOLDER := /home/pchrusciel/cncTools
DLIB_VERSION := 19.24

start_vnc:
	x11vnc -display :0

prepare_and_install: prepare_system prepare_python prepare_node prepare_resources install

prepare_system:
	sudo apt-get update \
	sudo apt-get install -y ffmpeg

prepare_node:
	sudo apt-get install curl -y \
	&& cd /tmp && curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash \
	&& source ~/.profile \
	&& nvm install 16 \
	&& nvm use 16 \
	&& npm install -g yarn

prepare_dlib:
	sudo apt-get install -y \
	cmake pkg-config libx11-dev libatlas-base-dev libgtk-3-dev libboost-python-dev \
	&& rm -rf tmp \
	&& mkdir tmp \
	&& cd tmp \
	&& wget http://dlib.net/files/dlib-${DLIB_VERSION}.tar.bz2 \
	&& tar xvf dlib-${DLIB_VERSION}.tar.bz2 \
	&& cd dlib-${DLIB_VERSION} \
	&& mkdir build && cd build \
	&& cmake .. && cmake --build . --config Release \
	&& sudo make install \
	&& sudo ldconfig \
	&& cd .. \
	&& pkg-config --libs --cflags dlib-1


prepare_dlib_python:
	cd tmp/dlib-${DLIB_VERSION} \
	&& python3 setup.py install

prepare_resources:
	sudo cp resources/nginx/cam.conf /etc/nginx/sites-available \
	sudo cp resources/nginx/sec.conf /etc/nginx/sites-available \
    && sudo ln -s /etc/nginx/sites-available/cam.conf /etc/nginx/sites-enabled \
    && sudo ln -s /etc/nginx/sites-available/sec.conf /etc/nginx/sites-enabled \
    && sudo service nginx restart

prepare_python:
	sudo apt install -y python3.7-dev python3-distutils uwsgi uwsgi-src uuid-dev libcap-dev libpcre3-dev libpython3.7-dev libpython3-all-dev uwsgi-plugin-python3 \
	&& pip3 install uwsgi

install: install_python_deps install_js_deps

install_python_deps:
	pip3 install -r requirements.txt

install_js_deps:
	yarn install

test_cam:
	python3 scripts/testcam.py

start_stream:
	python3 app.py

sync_cnc:
	rsync -av --exclude={'venv','.idea','__pycache__','node_modules','build'} ./ ${CNCUSER}@${CNCIP}:${CNCFOLDER}

start_uwsgi_cam:
	uwsgi resources/uwsgi/uwsgi_cam.ini --enable-threads

start_uwsgi_sec:
	uwsgi resources/uwsgi/uwsgi_sec.ini
