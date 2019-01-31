import network
from machine import Pin
import socket
import urllib
import time
import urequests as requests
import json
from machine import UART
u2=UART(0,115200)

def do_connect():
        sta_if = network.WLAN(network.STA_IF)
        p2 = Pin(2, Pin.OUT)
        sta_if.active(False)
        if not sta_if.isconnected():
                p2.value(0)
                print('connecting to network...')
                sta_if.active(True)
                sta_if.connect('TurnipSmart', 'turnip2016')
                while not sta_if.isconnected():
                        pass
        if sta_if.isconnected():
                print('connect success')
                p2.value(1)
                print('network config:', sta_if.ifconfig())

def	http_get(url):
	res=requests.get(url).text
	j=json.loads(res)
	list=j['sysTime2'].split()[1]
	print (list)
	
do_connect()

while True:
	http_get('http://quan.suning.com/getSysTime.do')
	time.sleep_ms(500)