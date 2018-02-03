#!/usr/bin/env python
# coding: utf-8

import os
from config_loader import load_global_conf

conf_dict = load_global_conf()


# '''mysql configuration'''
# MYSQL_SERVER = conf_dict["mysql_host"]
# MYSQL_USER = conf_dict["mysql_user"]
# MYSQL_PORT = int(conf_dict["mysql_port"])
# MYSQL_PASSWORD = conf_dict["mysql_pwd"]
# MYSQL_TYPE = conf_dict["mysql_type"]
# MYSQL_DB_MESSAGE = "siterec_center"
#
#
# '''redis configuration'''
# REDIS_IP = conf_dict["redis_online_host"]
# REDIS_PORT = conf_dict["redis_online_port"]
# REDIS_PASSWD = conf_dict["redis_online_pwd"]
# REDIS_TYPE = conf_dict["redis_online_type"]

LISTEN_PORT = 9092

settings = {
    'template_path': os.path.join('', 'templates')
}