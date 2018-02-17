import os

from tornado.ioloop import IOLoop
from tornado.web import Application

from sockets.websocket import WebSocket


if __name__ == '__main__':
    print("PYTHONPATH: {}".format(os.environ['PYTHONPATH']))
    server = Application([
        (r'/websocket/', WebSocket)
    ])

    print("Running server...")

    server.listen(5000)
    IOLoop.instance().start()