from simple import MQTTClient
from machine import Pin,I2C
import machine
import micropython
import json
import time
import urequests
i2c = I2C(scl=Pin(14), sda=Pin(2), freq=40000)
print(i2c.scan())

def read():
	i2c.start()
	try:
		hc=i2c.readfrom_mem(43,0,14,addrsize=8)
	except OSError:
		return
	l=(hc[0]<<24)|(hc[1]<<16)|(hc[2]<<8)|hc[3]
	t=((hc[4]<<8)|hc[5])/100
	p=((hc[6]<<24)|(hc[7]<<16)|(hc[8]<<8)|hc[9])/100
	h=((hc[10]<<8)|hc[11])/100
	H=((hc[12]<<8)|hc[13])
	i2c.stop()
	return l,t,p,h,H

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

def	sub_cb():
	a=0
	
def http_put_data(data,name):
	url='http://api.heclouds.com/devices/'+CLIENT_ID+'/datapoints'
	values={'datastreams':[{"id":name,"datapoints":[{"value":data}]}]}
	jdata = json.dumps(values)
	try:
		r=urequests.post(url,data=jdata,headers={"api-key":password})
	except OSError:
		pass
	r.text
	return r
		   
def main(server=SERVER):
	#端口号为：6002
	c = MQTTClient(CLIENT_ID, server,6002,username,password)
	c.set_callback(sub_cb)
	c.connect()
	c.subscribe(TOPIC)
	print("Connected to %s, subscribed to %s topic" % (server, TOPIC))
	while 1:
		# c.wait_msg()
		try:
			l,t,p,h,H=read()
			rsp = http_put_data(l,'light intensity')
			rsp = http_put_data(t,'temperature')
			rsp = http_put_data(p,'pressure')
			rsp = http_put_data(h,'humidity')
			rsp = http_put_data(H,'altitude')
			time.sleep(2)
		except TypeError:
			pass