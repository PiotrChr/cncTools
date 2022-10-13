from flask import Flask, Blueprint
import urllib3
import json

from config import config


http = urllib3.PoolManager()

notifications = Blueprint('notifications', __name__)
