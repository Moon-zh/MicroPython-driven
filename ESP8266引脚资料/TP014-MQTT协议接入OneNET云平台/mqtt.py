from simple import MQTTClient
from machine import Pin
import machine
import micropython
import json
import urequests
#选择G4引脚
g4 = Pin(4, Pin.OUT, value=0)
# MQTT服务器地址域名为：183.230.40.39,不变
SERVER = "183.230.40.39"
#设备ID
CLIENT_ID = "35135120"
#随便起个名字
TOPIC = b"TurnipRobot"
#产品ID
username='151303'
#产品APIKey:
password='uwklQQTsrDkqBWdTYtWwlHdj=Ys='
state = 0
def sub_cb(topic, msg):
	global state
	print((topic, msg))
	if msg == b"on":
			g4.value(1)
			state = 1
			print("1")
	elif msg == b"off":
			g4.value(0)
			state = 0
			print("0")
	elif msg == b"toggle":

			state = 1 - state
			g4.value(state)
			
def http_put_data(data):
	url='http://api.heclouds.com/devices/'+CLIENT_ID+'/datapoints'
	values={'datastreams':[{"id":"temperature","datapoints":[{"value":data}]}]}
	jdata = json.dumps(values)				   
	r=urequests.post(url,data=jdata,headers={"api-key":password})
	return r
		   
def main(server=SERVER):
	#端口号为：6002
	c = MQTTClient(CLIENT_ID, server,6002,username,password)
	c.set_callback(sub_cb)
	c.connect()
	c.subscribe(TOPIC)
	print("Connected to %s, subscribed to %s topic" % (server, TOPIC))
	try:
		while 1:
			c.wait_msg()
			rsp = http_put_data(86)
			print(rsp.json())
	finally:
			c.disconnect()