#!/usr/bin/env python
# coding=utf-8 
import pdb
import sys  
import time
sys.path.append('/home/hacker/Workspace/code/python/proxy_pool/')
import requests 
from bs4 import BeautifulSoup  
from Util.utilFunction import robustCrawl  

proxies = {
    'http':'socks5://127.0.0.1:9050',
    'https':'socks5://127.0.0.1:9050'
}

headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
        }

class GetFreeProxy():
    
    def __init__(self):
        pass

    @staticmethod 
    @robustCrawl
    def freeproxyfirst(page=1):
        base_url = 'http://www.xicidaili.com/nn/{page}'
        for i in range(page):
            url = base_url.format(page=i+1)
            r = requests.get(url,headers=headers) 
            soup = BeautifulSoup(r.text,'lxml') 
            table = soup.find(id='ip_list')

            ips = [i.contents[3].string for i in table.children if i != '\n'][1:]
            ports = [i.contents[5].string for i in table.children if i != '\n'][1:]
            for ip,port in zip(ips,ports):
                yield ':'.join((ip,port))


    @staticmethod
    @robustCrawl
    def freeproxysecond(page=10):
        base_url = 'http://www.mimiip.com/hw/{page}'
        for i in range(page):
            url = base_url.format(page=i+1)
            r = requests.get(url,proxies=proxies,headers=headers) 
            soup = BeautifulSoup(r.text,'lxml')
            table = soup.find('table') 

            ips = [i.contents[1].string for i in table.children if i != '\n'][1:]
            ports = [i.contents[3].string for i in table.children if i != '\n'][1:]
            if len(ips) != len(ports):
                continue

            for ip,port in zip(ips,ports):
                yield ':'.join((ip,port)) 


    @staticmethod
    @robustCrawl
    def freeproxythird(page=900):
        base_url = 'http://www.ip181.com/daili/{page}.html'
        for i in range(page):
            url = base_url.format(page=i+1)
            try:
                r = requests.get(url,headers=headers)
                time.sleep(1)
                soup = BeautifulSoup(r.content.decode('gb2312'),'lxml') 
                table = soup.find('table').contents[1]

                ips = [i.contents[1].string for i in table.children if i != '\n'][1:]
                ports = [i.contents[3].string for i in table.children if i != '\n'][1:]
                protocols = [i.contents[7].string for i in table.children if i != '\n'][1:]
                locations = [i.contents[11].string for i in table.children if i != '\n'][1:]

            except Exception as e:
#                print(e)
                continue

            if len(ips) != len(ports) or len(ips) != len(protocols) or len(ips) != len(locations):
                continue 
            
            print('第{}页完成'.format(i+1))

            for i in range(len(ips)):
                yield "('{}','{}','{}','{}',now())".format(ips[i],ports[i],protocols[i],locations[i])



if __name__=='__main__':
    gg = GetFreeProxy() 
    for i in gg.freeproxythird():
        print(i)
