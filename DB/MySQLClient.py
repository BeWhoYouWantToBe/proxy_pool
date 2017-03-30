#!/usr/bin/env python
# coding=utf-8
import pymysql 
import random  
import pdb

class MySQLClient():
    
    def __init__(self,host,uname,pwd,db):
        self.db = pymysql.connect(host,uname,pwd,db,charset='utf8') 
        self.cursor = self.db.cursor() 

    def get(self,table):
        self.cursor.execute('select * from {}'.format(table)) 
        data = self.cursor.fetchall() 
        return random.choice(data)

    def put(self,table,value):
        try:
            self.cursor.execute('insert ignore into {} values{}'.format(table,value))
            self.db.commit() 
        except Exception as e:
            print(e)


    def delete(self,table,value):
        self.cursor.execute('delete from {} where ip="{}"'.format(table,value))
        self.db.commit() 

    def pop(self,table):
        data = self.get(table) 
        self.delete(table,data[0]) 
        return data 


    def getAll(self,table):
        self.cursor.execute('select * from {}'.format(table))
        data = self.cursor.fetchall() 
        return data 
