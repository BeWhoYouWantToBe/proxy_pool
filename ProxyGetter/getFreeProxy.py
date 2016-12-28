#!/usr/bin/env python
# coding=utf-8
import sys 
sys.path.append('/home/stick/code/python/proxy_pool/')
import requests 
from bs4 import BeautifulSoup  
from Util.utilFunction import robustCrawl 

class GetFreeProxy():
    
    def __init__(self):
        pass 

    @staticmethod 
    @robustCrawl
    def freeproxyfirst(page=10):
        base_url = 'http://www.kuaidaili.com/proxylist/{page}'
        for i in range(page):
            url = base_url.format(page=i+1)
            r = requests.get(url) 
            soup = BeautifulSoup(r.text,'lxml') 
            ips = [i.string for i in soup.find_all(attrs={'data-title':'IP'})]
            ports = [i.string for i in soup.find_all(attrs={'data-title':'PORT'})]
            for ip,port in zip(ips,ports):
                yield ':'.join((ip,port))


if __name__=='__main__':
    gg = GetFreeProxy() 
    for i in gg.freeProxyFirst():
        print(i)
