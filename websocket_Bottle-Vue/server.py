"""This is a test program for using Websockrt at Bottle"""
from time import sleep
import random
import json
from datetime import datetime
from bottle import request, Bottle, abort, static_file
from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler

APP = Bottle()
SERVER = WSGIServer(("0.0.0.0", 8888), APP, handler_class=WebSocketHandler)

@APP.route('/websocket')
def handle_websocket():
    """
    WebSocket Handler
    Return count once every 3 seconds
    """
    websocket = request.environ.get('wsgi.websocket')

    if not websocket:
        abort(400, 'Expected WebSocket request.')

    while True:
        try:
            handler = websocket.handler
            for client in handler.server.clients.values():
                now_time = datetime.strftime(datetime.now(), '%H:%M:%S')
                random_num = random.randint(1, 100)
                print(now_time)
                print(random_num)
                data = {"time": now_time, "random": random_num}
                client.ws.send(json.dumps(data))

        except WebSocketError:
            break

        sleep(5)

@APP.route('/')
def top():
    """
    Returning WebSocket client when accessing localhost:8888/
    """
    return static_file('index.html', root='./')

SERVER.serve_forever()
