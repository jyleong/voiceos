import os

from tornado.ioloop import IOLoop
from tornado.web import Application

from sockets.websocket import WebSocket


if __name__ == '__main__':
    print("PYTHONPATH: {}".format(os.environ['PYTHONPATH']))
    server = Application([
        (r'/websocket/', WebSocket)
    ])

    print("Running server on port 5001...")

    server.listen(5001)
    IOLoop.instance().start()