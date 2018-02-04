#! /usr/bin/env python
# coding: utf-8
# author:zhihua

import traceback, logging, sys, random, requests
sys.path.append('../')
from conf import config
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Referer': 'https://www.kuaidaili.com',
    'Host': 'www.kuaidaili.com'
}


def parse_kuaidaili_proxy():
    try:
        url = config.PROXY_SITES.get('kuaidaili') % random.randint(1, 190)
        headers['Referer'] = 'https://www.kuaidaili.com'
        r = requests.get(url, headers=headers)
        bsoup = BeautifulSoup(r.content, 'html.parser')
        btable = bsoup.find('table', {'class': 'table table-bordered table-striped'})
        btbody = btable.find('tbody')
        proxy_list = []
        for btline in btbody.find_all('tr'):
            proxy_info = dict()
            proxy_info['ip'] = btline.find('td', {'data-title': 'IP'}).text.strip()
            proxy_info['port'] = btline.find('td', {'data-title': 'PORT'}).text.strip()
            proxy_info['spd'] = btline.find('td', {'data-title': '响应速度'}).text.replace('秒', 's')
            proxy_info['proxy'] = 'http://%s:%s' % (proxy_info['ip'], proxy_info['port'])
            proxy_list.append(proxy_info)
        return proxy_list
    except Exception as e:
        logging.error(traceback.format_exc())
        print traceback.format_exc()
        return []

if __name__ == "__main__":
    print parse_kuaidaili_proxy()

