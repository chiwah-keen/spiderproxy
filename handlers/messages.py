#! /usr/bin/env python
# coding: utf-8
# author:zhihua

import traceback
from base import BaseHandler


class MessagesHandler(BaseHandler):

    def post(self):
        mtype = self.get_argument('mtype', '')
        if not mtype:
            self.log.warn('mtype required !')
            yield self.send_status_message(-1, 'mtype required!')
        self.params = self.get_json()
        if mtype == "wfdt": # 我方动态
            self.operate_wfdt()
        elif mtype == "zcqbl": # 战场情报
            yield self.operate_zcqbl()
        elif mtype == "rwdt": # 任务动态
            self.operate_rwdt()
        elif mtype == "zzcl": # 战场策略
            self.operate_zzcl()
        else:
            self.log.warn('invalid mtype %s' % mtype)
            self.send_status_message(-1, 'invalid mtype!')

    def operate_wfdt(self):
        try:
            return True
        except Exception as e:
            self.log.error(traceback.format_exc())
            return False

    def operate_zcqbl(self):
        try:
            return True
        except Exception as e:
            self.log.error(traceback.format_exc())
            return False

    def operate_rwdt(self):
        try:
            return True
        except Exception as e:
            self.log.error(traceback.format_exc())
            return False

    def operate_zzcl(self):
        try:
            return True
        except Exception as e:
            self.log.error(traceback.format_exc())
            return False
