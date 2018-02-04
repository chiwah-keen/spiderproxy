#! /usr/bin/env python
# coding: utf-8
# author:zhihua

import socket


def get_local_ipaddr():
    n = socket.getfqdn(socket.gethostname())
    return socket.gethostbyname(n)

if __name__ == "__main__":
    print get_local_ipaddr()
