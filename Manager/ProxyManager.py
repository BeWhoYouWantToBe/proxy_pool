#!/usr/bin/env python
# coding=utf-8 
import sys 
import os 
sys.path.append(os.path.dirname(sys.path[0]))

from DB.DbClient import DbClient 
from Util.GetConfig import GetConfig  
from ProxyGetter.getFreeProxy import GetFreeProxy 

class ProxyManager():
    
    def __init__(self):
        self.db = DbClient() 
        self.config = GetConfig() 
        self.raw_proxy_queue = 'raw_proxy' 
        self.useful_proxy_queue = 'useful_proxy_queue' 

    def refresh(self):
        for proxyGetter in self.config.proxy_getter_functions():
            proxy_set = set() 
            for proxy in getattr(GetFreeProxy,proxyGetter.strip())():
                proxy_set.add(proxy) 

            for proxy in proxy_set:
                self.db.put('raw_proxy',proxy) 

    def get(self):
        return self.db.pop('useful_proxy')

    def delete(self,proxy):
        self.db.delete('useful_proxy',proxy)

    def getAll(self):
        return self.db.getAll('useful_proxy')

if __name__ == '__main__':
    pp = ProxyManager() 
    pp.refresh() 
