#!/usr/bin/env python
# coding: utf-8

import os


def load_global_conf():
    conf_dict = {}
    if os.path.exists("/run/secrets/global.conf"):
        with open("/run/secrets/global.conf") as infile:
            for line in infile:
                if not line or line.startswith("#") or line.find("=") == -1:
                    continue
                tlist = line.strip().split('=')
                if len(tlist) != 2:
                    continue
                key, val = tlist
                conf_dict[key] = val
    return conf_dict