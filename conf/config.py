#!/usr/bin/env python
# coding: utf-8

import os
from config_loader import load_global_conf

conf_dict = load_global_conf()


LISTEN_PORT = 5001
PROXY_SITES = {
    'kuaidaili': 'https://www.kuaidaili.com/free/inha/%s/',
}





settings = {
    'template_path': os.path.join('', 'templates')
}