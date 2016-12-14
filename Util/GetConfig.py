#!/usr/bin/env python
# coding=utf-8
import os  
from configparser import ConfigParser 

class GetConfig():

    def __init__(self):
        self.pwd = os.path.split(os.path.realpath(__file__))[0] 
        self.config_path = os.path.join(os.path.split(self.pwd)[0],'Config.ini') 
        self.config_file = ConfigParser() 
        self.config_file.read(self.config_path) 

    def db_type(self):
        return self.config_file.get('DB','type') 

    def db_name(self):
        return self.config_file.get('DB','name') 

    def db_host(self):
        return self.config_file.get('DB','host') 

    def db_port(self):
        return self.config_file.get('DB','port') 

    def proxy_getter_functions(self):
        return self.config_file.options('ProxyGetter')
    

if __name__ == '__main__':
    gg = GetConfig() 
    print(gg.db_type()) 
    print(gg.db_name()) 
    print(gg.proxy_getter_functions())



