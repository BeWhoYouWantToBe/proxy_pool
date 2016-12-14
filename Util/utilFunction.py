#!/usr/bin/env python
# coding=utf-8

def robustCrawl(func):
    def decorate(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            print('sorry,sth wrong,the reason is:')
            print(e)

    return decorate
