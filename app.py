#! /usr/bin/env python
# coding: utf-8
# author:zhihua

import sys
import socket
from tornado import httpserver, ioloop
from tornado import web
from conf import config
from log import Log
socket.setdefaulttimeout(0.3)
reload(sys)
sys.setdefaultencoding('utf-8')


routes = [
         (r"/",                    "handlers.proxy.ProxyNoteHandler"),
         (r"/proxy/list",          "handlers.proxy.ProxyListHandler"),
          ]


class Application(web.Application):
    def __init__(self):
        web.Application.__init__(self, routes, **config.settings)
        self.log = Log("./logs/", name='bfbq', dividelevel=0, loglevel='info')
        self.caches = {}


def start():
    application = Application()
    http_server = httpserver.HTTPServer(application)
    http_server.listen(config.LISTEN_PORT)
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    start()