#!/usr/bin/env python
# coding=utf-8
import os
import sys 
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Util.GetConfig import GetConfig 

class DbClient():

    def __init__(self):
        self.config = GetConfig() 
        self.__initDbClient() 

    def __initDbClient(self):
        __type = None 
        if 'MySQL' == self.config.db_type():
            __type = 'MySQLClient'
        else:
            print('type error,Not support DB type: {}'.format(__type))
        
        self.client = getattr(__import__(__type),__type)(host=self.config.db_host(),uname=self.config.db_uname(),pwd=self.config.db_pwd(),db=self.config.db_name())

    def get(self,*args):
        return self.client.get(*args)

    def put(self,*args):
        return self.client.put(*args) 

    def delete(self,*args):
        return self.client.delete(*args)

    def pop(self,*args):
        return self.client.pop(*args)

    def getAll(self,*args):
        return self.client.getAll(*args)

if __name__ == '__main__':
    db = DbClient() 
    db.put('raw_proxy','127.0.0.1:8080')
    db.delete('raw_proxy','127.0.0.1:8080')
    db.pop('raw_proxy')
    print(db.getAll('raw_proxy'))
