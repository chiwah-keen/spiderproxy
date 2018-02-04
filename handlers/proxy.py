#! /usr/bin/env python
# coding: utf-8
# author:zhihua

from base import BaseHandler
from conf import config
import utils, uuid, time, traceback, proxyparser


class ProxyNoteHandler(BaseHandler):

    def get(self):
        try:
            local_ip = utils.get_local_ipaddr()
            user_id = str(uuid.uuid4()).replace('-', '')
            rst_dict = dict()
            for k, v in config.PROXY_SITES.items():
                rst_dict[k] = 'http://%s:%s/proxy/list?ptype=%s&uid=%s&ttl=%s' % \
                              (local_ip, config.LISTEN_PORT, k, user_id, 300)
            self.send_data(rst_dict)
        except Exception as e:
            self.log.error(traceback.format_exc())
            self.send_status_message(-1, traceback.format_exc())


class ProxyListHandler(BaseHandler):

    def get(self):
        try:
            uid = self.get_argument('uid', '')
            ptype = self.get_argument('ptype', '')
            ttl = self.get_argument('ttl', 300)
            ttl = int(ttl)
            if not uid or not config.PROXY_SITES.get(ptype.strip()):
                return self.send_status_message(1, 'invalid uid or type')
            if uid not in self.caches: self.caches[uid] = {}
            proxies = self.get_proxy(uid, ptype, ttl)
            if not proxies:
                return self.send_status_message(-1, 'error!')
            self.send_data(proxies)
        except Exception as e:
            self.log.error(traceback.format_exc())
            self.send_status_message(-1, traceback.format_exc())

    def get_proxy(self, uid, ptye, ttl):
        if self.caches.get(uid) and int(time.time()) - self.caches[uid]['timestamp'] < ttl:
            self.caches[uid]['ttl'] = ttl
            print 2
            return self.caches[uid]['proxies']
        print 1
        proxies = self.get_site_proxy(ptye)
        if not proxies: return []
        self.caches[uid] = {'timestamp': int(time.time()),
                            'proxies': proxies,
                            'ttl': ttl}
        return proxies

    def get_site_proxy(self, sitename):
        # kuaikan 代理
        if sitename == "kuaidaili":
            data = []
            for i in range(5):
                data = proxyparser.parse_kuaidaili_proxy()
                if data: break
            return data
        # todo xicidaili 代理
        return []



