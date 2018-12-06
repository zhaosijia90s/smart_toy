from flask import Flask,request
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from geventwebsocket.websocket import WebSocket
import json

ws_app = Flask(__name__)

socket_dict = {}
@ws_app.route('/app/<app_id>')
def app(app_id):
