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
        ip,port,protocol,location,t = self.db.pop('raw_proxies')
        while ip:
            proxies = {'http':'http://{}:{}'.format(ip,port),
                       'https':'http://{}:{}'.format(ip,port)}
            try:
                r = requests.get('https://www.icanhazip.com',proxies=proxies,timeout=20,verify=False)
                if r.text.strip() == ip:
                    self.db.put('useful_proxies',"('{}','{}','{}','{}','{}')".format(ip,port,protocol,location,t))
                    print(ip+' OK')

            except Exception as e:
#                print(e)
                print(ip+' ERROR')

            ip,port,protocol,location,t = self.db.pop('raw_proxies')

def refreshPool():
    pp = ProxyRefreshSchedule() 
    pp.validProxy() 

def main(process_num=50):
    p = ProxyRefreshSchedule() 
    p.refresh() 

    pool = Pool(process_num) 
    for i in range(process_num):
        pool.apply_async(refreshPool)
    pool.close() 
    pool.join() 

    print('{}: refresh complete!'.format(time.ctime()))


if __name__ == '__main__':
    main() 
