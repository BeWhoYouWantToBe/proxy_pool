#!/usr/bin/env python
# coding=utf-8
import sys 
sys.path.append('../')
from flask import Flask,jsonify,request
from Manager.ProxyManager import ProxyManager 

app = Flask(__name__)

api_list = {
    'get':'get an usable proxy',
    'refresh':'refresh proxy pool',
    'get_all':'get all proxy from proxy pool',
    'delete/ip':'delete an unable proxy',
}

@app.route('/') 
def index():
    return jsonify(api_list)

@app.route('/get/') 
def get():
    proxy = ProxyManager().get() 
    return jsonify(list(proxy))

@app.route('/refresh/')
def refresh():
    ProxyManager().refresh() 
    return 'success' 

@app.route('/getAll/')
def getAll():
    proxies = ProxyManager().getAll() 
    return jsonify(list(proxies))

@app.route('/delete/<ip>')
def delete(ip):
    ProxyManager().delete(ip)
    return 'success'

'''@app.route('/delete/',methods=['GET'])
def delete():
    ip = request.args.get('ip')
    ProxyManager().delete(ip) 
    return 'success'  '''



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True) 
