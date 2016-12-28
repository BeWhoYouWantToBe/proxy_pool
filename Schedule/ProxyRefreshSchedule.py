#!/usr/bin/env python
# coding=utf-8
from apscheduler.schedulers.blocking import BlockingScheduler 
from multiprocessing.dummy import Pool
import requests 
import time 
import sys 
import os 
import pdb

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Manager.ProxyManager import ProxyManager 

class ProxyRefreshSchedule(ProxyManager):

    def __init__(self):
        ProxyManager.__init__(self)

    def validProxy(self):
        raw_proxy = self.db.pop('raw_proxy')
        while raw_proxy:
            proxies = {'http':'http://{}'.format(raw_proxy),
                       'https':'https://{}'.format(raw_proxy)}
            try:
                r = requests.get('http://www.icanhazip.com',proxies=proxies,timeout=5,verify=False)
                if r.status_code == 200:
                    self.db.put('useful_proxy',raw_proxy)
            except Exception as e:
                pass 
            raw_proxy = self.db.pop('raw_proxy')

def refreshPool():
    pp = ProxyRefreshSchedule() 
    pp.validProxy() 

def main(process_num=50):
    p = ProxyRefreshSchedule() 
    p.refresh() 

    pool = Pool(50) 
    for i in range(process_num):
        pool.apply_async(refreshPool)
    pool.close() 
    pool.join() 

    print('{}: refresh complete!'.format(time.ctime()))


if __name__ == '__main__':
    main() 
