#!/usr/bin/env python
# coding=utf-8
import pymysql 
import random  
import pdb

class MySQLClient():
    
    def __init__(self,host,uname,pwd,db):
        self.db = pymysql.connect(host,uname,pwd,db) 
        self.cursor = self.db.cursor() 

    def get(self,table):
        self.cursor.execute('select * from {}'.format(table)) 
        data = self.cursor.fetchall() 
        return random.choice(data)[0]

    def put(self,table,value):
        self.cursor.execute('insert into {} values("{}")'.format(table,value))
        self.db.commit() 

    def delete(self,table,value):
        self.cursor.execute('delete from {} where proxys="{}"'.format(table,value))
        self.db.commit() 

    def pop(self,table):
        data = self.get(table) 
        self.delete(table,data) 
        return data 


    def getAll(self,table):
        self.cursor.execute('select * from {}'.format(table))
        data = self.cursor.fetchall() 
        return data 
